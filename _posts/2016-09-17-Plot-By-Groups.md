---
layout: post
title: Plotting by groups using Matplotlib, Seaborn, and Pandas
---


![png](/images/2016-09-17-Plot-By-Groups_files/2016-09-17-Plot-By-Groups_41_0.png)

Data visualization is one of the most important aspects of preparing a paper, presentation or poster. However, it's often treated as an afterthought in data analysis. Us humans are remarkably good at interpreting visual data and finding patterns, so why not use this to our advantage when it comes to solving problems? Apparently I'm not alone in thinking this way. I've recently discovered [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/), a fantastic library for making practical, aesthetically pleasing graphs. I've also recently been playing around with the [pandas](http://pandas.pydata.org/) data analysis library, and I got inspired to try to combine these tools into something neat and useful. 


## Motivation
Let's say we have a few methods for calculating something, and a few systems on which we want to use each method. Potentially there's a third layer of variables: maybe we're having a bunch of students run the calculations. This type of problem can pop up all over the place and plotting each figure manually can be a bit painful, particularly if you have to keep changing it. I think it would be nice to have a quick way to produce high quality plots instantly so that they can be quickly updated if need be. 

## 1) Boilerplate
---


```python
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```

## 2) Get Data
---

Now if you already have data, just load it up using some of the pandas built-in functions. I'm just gonna make up some! Suppose we have data from 4 methods, each with 4 systems being studied, and each of both of these is being calculated by every one of 2 students:


```python
NMethods = 4
NSystems = 4
NStudents  = 16

# Here's some numbers, in real life maybe loaded 
# directly from csv -> dataframe
def generate_data(Nmethods, NSystems, NStudents):
    x = np.linspace(0,1,100)
    Systems_y = np.asarray([20*i + 1 for i in range(NMethods)])
    Methods_y = np.asarray([5 * x * (i+1) for i in range(NSystems)])
    Students_y  = np.asarray([-4*x*x*(i+1) for i in range(NStudents)])

    # Just Name everything Method # ...
    Methods  = ['Method ' + str(i+1) for i in range(NMethods)]
    Systems  = ['System ' + str(i+1) for i in range(NSystems)]
    Students = ['Student ' + str(i+1) for i in range(NStudents)]

    # If you have real data this part is not needed
    data = []
    for i in range(NMethods):
        for j in range(NSystems):
            for k in range(NStudents):
                # Again made up y values
                y = Methods_y[i] + Systems_y[j] + Students_y[k] 
                # Let's make our data into a list of lists, there
                # are a few possibilities here
                data_row = [Methods[i], Systems[j], Students[k], x, y]
                data.append(data_row)
    return data

data = generate_data(NMethods, NSystems, NStudents)
```

## 3) Convert Data to Convenient Form
---

This is where pandas comes in handy. The [pandas DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) object has a ton of useful features that we will be using gratuitously, so let's load up some data  and get it into a format that pandas can use:


```python
cols = ['Method', 'System', 'Student', 'X', 'Y']
df = pd.DataFrame(data, columns=cols)
```

You can index the dataframe like so:


```python
df[:3] 
```


```python
>>>      Method      System      Student     X                               Y
>>> 0  'Method 1'  'System 1'  'Student 1' [0.0, 0.01, 0.020, 0.030, ...]  [1.0, 1.04, 1.08, 1.12, ...]
>>> 1  'Method 1'  'System 1'  'Student 2' [0.0, 0.01, 0.020, 0.030, ...]  [1.0, 1.01, 1.09, 1.44, ...]
>>> 2  'Method 1'  'System 1'  'Student 3' [0.0, 0.01, 0.020, 0.030, ...]  [1.0, 1.05, 1.10, 1.14, ...]
```

You can also index by name of column:


```python
df['Student'][:3]
```



```python
>>> 0    'Student 1'
>>> 1    'Student 2'
>>> 2    'Student 3'
>>> Name: Student, dtype: object
```


And you can even find all the rows for a particular student! We will be making use of these aspects of the pandas DataFrame!


```python
mask = df['Student'] == 'Student 7'
df[mask][:3]
```



```python
>>>      Method      System      Student     X                               Y
>>> 6  'Method 1'  'System 1'  'Student 7' [0.0, 0.01, 0.020, 0.030, ...]  [1.0, 1.04, 1.089, 1.125, ...]
>>> 22 'Method 1'  'System 2'  'Student 7' [0.0, 0.01, 0.020, 0.030, ...]  [21., 21.0, 21.0, 21.1,   ...]
>>> 38 'Method 1'  'System 3'  'Student 7' [0.0, 0.01, 0.020, 0.030, ...]  [41., 41.0, 41.0, 41.1,   ...]
```

## 4) Plot By groups
---

Ok here comes the fun stuff! This got a bit more complex than I thought it would at first, but I've gotten it to work pretty well. The general idea is to group the data by one (or more) of the 3 categories and apply the same color or style to each member of that group. Additionally, we can group once more into matplotlib's subplots (this is why I chose 3 possible groupings, but don't tell anybody!).

### 4a) Create the Class
---

About half way through writing this, I figured out that it makes a lot more sense to write it in an object oriented style. Let's make the class, have it initialize with a dataframe, the labels for x and y values in the dataframe, and set some default values. 


```python
class GroupPlot(object):
    
    def __init__(self, DataFrame, x, y):
        self.df = DataFrame
        self.x  = x
        self.y  = y
        self.set_defaults()
               
    def set_defaults(self):
        self.color_by  = None
        self.style_by  = None
        self.subplt_by = None
        self.subplt_cols = None
        self.fig_legend = None
        self.styles = None
```

Here I'm letting the user choose several options. We'll make it so that they can choose whether or not to group by colors, styles or subplots. The *self.subplt_cols* option is to set the number of columns used in the subplot, but is not needed. Finally the user can submit a list of styles that matplotlib will use to draw the lines (such a
s ['-', '..']).

### 4b) Determine number of entries per category
--- 
Ok, now that the defaults are set, let's get into the meat of the program. First, we need to know how many items are contained in each grouping. This is where I'm using panda's [indexing options](http://pandas.pydata.org/pandas-docs/stable/indexing.html) to index a column of the data frame based on the string that labels it. Then the *.unique()* function removes duplicated entries. What I'm left with is a list of the unique entries in that column:


```python
df['Method'].unique()
```
```python
>>> array(['Method 1', 'Method 2', 'Method 3', 'Method 4'], dtype=object)
```


Then the number of Methods I have is simply the length of this list. So  let's make lists that contain the categories of every row, which we will be using as dictionary keys later. To get the numbers of each category just take the the number of unique elements in that list. 


```python
def get_numbers(self):
    if self.color_by:
        self.color_keys = self.df[self.color_by]
        self.Ncolors = len(self.color_keys.unique())
    if self.style_by:
        self.style_keys = self.df[self.style_by]
        self.Nstyles = len(self.style_keys.unique())
    if self.subplt_by:
        self.subplt_keys = self.df[self.subplt_by]
        self.Nsubplt = len(self.subplt_keys.unique())
```

### 4c) Determine Colors
---

I decided to use a dictionary for this part. Basically all this function does is remake a color scheme if more than 6 are needed, then construct a dictionary *color_dic*. The dictionary contains the unique entries in the *self.color_by* column, and map them to the entries of the [seaborn color palette](https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.color_palette.html). This way the user can define any colorscheme they want, by changing the color palette using the [set_palette](https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.set_palette.html) function. 


```python
def get_color_dic(self):
    if self.color_by:
        if self.Ncolors > 6:
            #Default only has 6 colors, make new one if needed
            sns.set_palette(sns.color_palette("hls", self.Ncolors))
        color_dic = {}
        for i, key in enumerate(self.color_keys.unique()):
            color_dic[key] = sns.color_palette()[i]
        self.color_dic = color_dic
```

### 4d) Determine Styles
---

Matplotlib has 4 linestyle options, If the user requests too many styles, throw an error


```python
def check_styles(self):
    if self.style_by:
        if not self.styles:
            self.styles = ['-', '--','-.', ':',]
        if  self.Nstyles > len(self.styles):
            raise ValueError('# of styles needed exceeds #'
                            + 'of styles available: currently '
                            + str(len(self.styles)) + ', needs ' 
                            + str(self.Nstyles) + '.')
```

Just like the color dictionary, make a dictionary for the line styles:


```python
def get_style_dic(self):
    if self.style_by:
        style_dic = {}
        for i, key in enumerate(self.style_keys.unique()):
            style_dic[key] = self.styles[i]
        self.style_dic = style_dic
```

### 4e) Determine subplot info
---

In order to draw the subplots, we need to know how many rows and columns we want. We let the user specify the number of columns if they want, but by default I thought it made sense to try to get as close to a square as possible. I did this by taking the total number of subplots requested, square rooting it and rounding down to the nearest integer. By rounding down we ensure that the plot will add rows before it adds more columns, which I think looks nicer. 

If our plots don't form a nice rectangle, we add one row and fill it in from there!


```python
def get_subplot_params(self):
    if self.subplt_by:
        if not self.subplt_cols:
            subplt_cols = int(math.floor(np.sqrt(self.Nsubplt)))
        subplt_rows = self.Nsubplt / subplt_cols
        if self.Nsubplt % subplt_cols != 0:
            subplt_rows += 1
        self.subplt_rows = subplt_rows
        self.subplt_cols = subplt_cols
```

### 4f) Make the plots
---

Ok so now we have all of the parameters ready to go. Let's get to plotting! We'll be using the *self.lines* and *self.labels* attributes later to make a legend. I chose to iterate through each row of the data frame, and plot its x and y values according to the color, style and subplot given in the corresponding dictionaries. This one's a bit long, but I've tried to write it as clearly as possible. 


```python
def make_plots(self):
    self.lines = []
    self.labels = []
    for i in range(self.df.shape[0]):
        if self.subplt_by:
            subplot_val = self.sub_dic[self.subplt_keys[i]]
        else:
            subplot_val = [1,1,1]  # If not subplots, just 1 plot

        llabel = ''
        if self.style_by:
            lstyle = self.style_dic[self.style_keys[i]]
            llabel += self.style_keys[i]
            if self.color_by:
                llabel += ', ' # If we have style and color use , 
        else:
            lstyle = ''
            
        if self.color_by:    
            col = self.color_dic[self.color_keys[i]]
            llabel += self.color_keys[i]
        else:
            col = sns.color_palette()[0]

        self.labels.append(llabel)

        ax = fig.add_subplot(subplot_val[0], 
                             subplot_val[1], 
                             subplot_val[2])

        self.lines.append(ax.plot(self.df[self.x][i], 
                                  self.df[self.y][i], 
                                  lstyle, c=col, label=llabel))
        if self.subplt_by:
            plt.title(self.subplt_keys[i])
        plt.xlabel(self.x)
        plt.ylabel(self.y)
```

### 4e) Make the Figure Legend
---

If you were to just use plt.figure() at the end of the code, you get a single legend in the last entry of the subplots. Since we're categorizing and the same type of lines will have the same color and style across each subplot, it makes sense to use one legend for all of them. This is done using matplotlib's [figlegend](http://matplotlib.org/examples/pylab_examples/figlegend_demo.html) command. Since we've stored all the lines and labels in lists, we just have to make a list of the unique labels, and only generate legend entries for those (ignore any that turn out empty!). Then we just have to set the location:


```python
def get_figlegend(self):
    unique_labels = []
    unique_lines  = []
    for i, label in enumerate(self.labels):
        if label not in unique_labels and label != '':
            unique_labels.append(label)
            unique_lines.append(self.lines[i][0])

    plt.figlegend((unique_lines), unique_labels, 
                  bbox_to_anchor=(1.01, 0.5), loc='center left')
```

### 4f) Plot!
---

Finally, lets wrap up the method into a nice plot function:


```python
def plot(self):
    self.get_numbers()
    self.get_subplot_params()
    self.check_styles()
    self.get_style_dic()
    self.get_color_dic()
    self.get_sub_dic()
    self.make_plots()
    if self.fig_legend:
        self.get_figlegend()
```

### 4g) Done!
---

Ok that took some time, but here's the class in its entirety:


```python
class GroupPlot(object):
    
    def __init__(self, DataFrame, x, y):
        self.df = DataFrame
        self.x  = x
        self.y  = y
        self.set_defaults()
               
    def set_defaults(self):
        self.color_by  = None
        self.style_by  = None
        self.subplt_by = None
        self.subplt_cols = None
        self.fig_legend = None
        self.styles = None
 
    def get_numbers(self):
        if self.color_by:
            self.color_keys = self.df[self.color_by]
            self.Ncolors = len(self.color_keys.unique())
        if self.style_by:
            self.style_keys = self.df[self.style_by]
            self.Nstyles = len(self.style_keys.unique())
        if self.subplt_by:
            self.subplt_keys = self.df[self.subplt_by]
            self.Nsubplt = len(self.subplt_keys.unique())
        
    def get_color_dic(self):
        if self.color_by:
            if self.Ncolors > 6:
                #Default only has 6 colors, make new one if needed
                sns.set_palette(sns.color_palette("hls", self.Ncolors))
            color_dic = {}
            for i, key in enumerate(self.color_keys.unique()):
                color_dic[key] = sns.color_palette()[i]
            self.color_dic = color_dic

    def check_styles(self):
        if self.style_by:
            if not self.styles:
                self.styles = ['-', '--','-.', ':',]
            if  self.Nstyles > len(self.styles):
                raise ValueError('# of styles needed exceeds #'
                                + 'of styles available: currently '
                                + str(len(self.styles)) + ', needs ' 
                                + str(self.Nstyles) + '.')
            
    def get_style_dic(self):
        if self.style_by:
            style_dic = {}
            for i, key in enumerate(self.style_keys.unique()):
                style_dic[key] = self.styles[i]
            self.style_dic = style_dic
    
    def get_subplot_params(self):
    #Try to get close to a square layout by default
        if self.subplt_by:
            if not self.subplt_cols:
                subplt_cols = int(math.floor(np.sqrt(self.Nsubplt)))
            subplt_rows = self.Nsubplt / subplt_cols
            if self.Nsubplt % subplt_cols != 0:
                subplt_rows += 1
            self.subplt_rows = subplt_rows
            self.subplt_cols = subplt_cols
            
    def get_sub_dic(self):
        if self.subplt_by:
            sub_dic = {}
            for i, key in enumerate(self.subplt_keys.unique()):
                sub_dic[key] = [self.subplt_rows, self.subplt_cols, i+1]
            self.sub_dic = sub_dic

    def make_plots(self):
        self.lines = []
        self.labels = []
        for i in range(self.df.shape[0]):
            if self.subplt_by:
                subplot_val = self.sub_dic[self.subplt_keys[i]]
            else:
                subplot_val = [1,1,1]  # If not subplots, just 1 plot
            
            llabel = ''
            if self.style_by:
                lstyle = self.style_dic[self.style_keys[i]]
                llabel += self.style_keys[i]
                if self.color_by:
                    llabel += ', '
            else:
                lstyle = ''
            if self.color_by:    
                col = self.color_dic[self.color_keys[i]]
                llabel += self.color_keys[i]
            else:
                col = sns.color_palette()[0]
            
            
            self.labels.append(llabel)
            
            ax = fig.add_subplot(subplot_val[0], 
                                 subplot_val[1], 
                                 subplot_val[2])

            self.lines.append(ax.plot(self.df[self.x][i], 
                                      self.df[self.y][i], 
                                      lstyle, c=col, label=llabel))
            if self.subplt_by:
                plt.title(self.subplt_keys[i])
            plt.xlabel(self.x)
            plt.ylabel(self.y)
            
    def get_figlegend(self):
        unique_labels = []
        unique_lines  = []
        for i, label in enumerate(self.labels):
            if label not in unique_labels and label != '':
                unique_labels.append(label)
                unique_lines.append(self.lines[i][0])

        plt.figlegend((unique_lines), unique_labels, 
                      bbox_to_anchor=(1.01, 0.5), loc='center left')
      
    def plot(self):
        self.get_numbers()
        self.get_subplot_params()
        self.check_styles()
        self.get_style_dic()
        self.get_color_dic()
        self.get_sub_dic()
        self.make_plots()
        if self.fig_legend:
            self.get_figlegend()
```

## 5) Use!
---
Let's go back to our original problem. To use the function, all we need to do is get our data into a pandas DataFrame, and create a *GroupPlot* instance. Then we specify what type of groupings we want, and that's it! I've added a few formatting specifiers to make it look a bit better. 


```python
data = generate_data(NMethods, NSystems, NStudents)
cols = ['Method', 'System', 'Student', 'X', 'Y']
df = pd.DataFrame(data, columns=cols)
fig = plt.figure(figsize=(8,8))
x = GroupPlot(df, 'X', 'Y')
x.color_by  = 'System' 
x.style_by  = 'Method'
x.subplt_by = 'Student'
x.fig_legend= True
x.plot()
sns.despine()
plt.tight_layout()
plt.show()
```


![png](/images/2016-09-17-Plot-By-Groups_files/2016-09-17-Plot-By-Groups_37_0.png)


We can change which way we want to group the data easily:


```python
data = generate_data(NMethods, NSystems, NStudents)
cols = ['Method', 'System', 'Student', 'X', 'Y']
df = pd.DataFrame(data, columns=cols)
fig = plt.figure(figsize=(8,8))
x = GroupPlot(df, 'X', 'Y')
x.color_by  = 'Method'   # Switched method and system
x.style_by  = 'System'
x.subplt_by = 'Student'
x.fig_legend= True
x.plot()
sns.despine()
plt.tight_layout()
plt.show()
```


![png](/images/2016-09-17-Plot-By-Groups_files/2016-09-17-Plot-By-Groups_39_0.png)


And we can style using anything from matplotlib or seaborn, pretty cool! I'm a huge fan of the [xckd()](http://matplotlib.org/xkcd/examples/showcase/xkcd.html) function! 


```python
data = generate_data(NMethods, NSystems, NStudents)
cols = ['Method', 'System', 'Student', 'X', 'Y']
df = pd.DataFrame(data, columns=cols)
fig = plt.figure(figsize=(8,8))
plt.xkcd()
x = GroupPlot(df, 'X', 'Y')
x.color_by  = 'System' 
x.style_by  = 'Method'
x.subplt_by = 'Student'
x.fig_legend= True
x.plot()
sns.despine()
plt.tight_layout()
plt.show()
```


![png](/images/2016-09-17-Plot-By-Groups_files/2016-09-17-Plot-By-Groups_41_0.png)


## Conclusion
---

I've spent a good amount of time trying to figure this out, and I'm pretty happy with the results. One of the things I might play around with is getting a legend that has only a list of colors, and a list of linestyles (rather than all combinations). I don't think this would be too hard to implement, watch out for updates. 
