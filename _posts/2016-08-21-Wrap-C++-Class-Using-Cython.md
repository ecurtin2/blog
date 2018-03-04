---
layout: post
title: Wrapping a C++ Class in Python Using Cython
---

```python
import C++
```


One of my favorite uses for Cython is to use it to wrap a C++ class in python.
The reason I like this so much is that you can easily create a class in python,
and seamlessly optimize the slow parts in C++. This way you can get all the
advantages of python, like the easy syntax and massive amount of libraries that
are trivial to implement, while still being able to speed up performance critical
 sections of your code. However, at the end of the day, the resulting class
still looks like a standard python class, just better!

Now there is a tutorial on [wrapping C++ in the Cython documentation](http://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html),
which looks pretty good in retrospect. However, I struggled a bit when I was
trying to learn how to do this, so I decided to write this post to help anybody
else in my situation. Enough blabbering though, let's get to it!

# Step 1: Create the C++ Class
---
Let's say we defined a C++ class in the following header file, Class.h. I've
made the class pretty trivial for the purpose of demonstration:

## Class.h
{% highlight cpp  %}
#ifndef CPP_MYCLASS // header guards
#define CPP_MYCLASS

namespace my_namespace {
    class MyCppClass {
        public:
            //Attributes
            double cpp_double;
            double cpp_public;
            //Methods
            double cpp_func(double, int);
            void   cpp_void_func();
    };
}
#endif
{% endhighlight %}

In addition to the header file, we have defined the following implementation of
the class methods in Class.cpp:

## Class.cpp
{% highlight cpp  %}
#include "Class.h"

double my_namespace::MyCppClass::cpp_func(double x, int i) {
    double val = 0.0;
    for (int j = 0; j < i; j++) {
        val += x;
    }
    return val;
}

void my_namespace::MyCppClass::cpp_void_func() {
    cpp_double = 1.2;
}
{% endhighlight %}

Again the functions here are simple, but they can be any valid C++ function
(there are caveats which are discussed in Cython's documentation, but I haven't
had problems).  


# Step 2: Wrap the Class using Cython
---

Now this part is the meat of the problem. At first it's a bit intimidating and
confusing to see all these variable declarations in the cpp, header and pyx
files. Once you get a handle on it it's not too bad though. Additionally, the
redundant variable declarations could be automated (I might do this in a future
post).

## ClassWrapper.pyx

__*Note:*__ All the code in step 2 goes into *ClassWrapper.pyx*

First, we have to let Cython know that the class *MyCppClass* is defined inside
the file *Class.h*. The keyword *extern* here lets us know that the class is
defined elsewhere (ie. in the header file). Using this keyword in Cython like
this implies the entire class and all attributes/methods within are defined
externally in *Class.h*. Note that only methods/attributes that want python
access need to be here.

The *except +* part allows Cython to handle exceptions from the constructor.
Apart from this, the class definition is identical to the one in *Class.h*,
except for there is no ; at the end of each line.

{% highlight cpp  %}
cdef extern from "Class.h" namespace "my_namespace":

    cdef cppclass MyCppClass:
        MyCppClass() except +
        #Attributes
        double cpp_double
        double cpp_public

        #Methods
        double cpp_func(double x, int i)
        void cpp_void_func()
{% endhighlight %}

### Create the Wrapper Class

Ok, so we've told Cython that *MyCppClass* is defined elsewhere. If we want
python access to the class (which we do, if you've read this far) we have to
create a wrapper class around the C++ class. I treat this first portion as
boilerplate, it allows us to allocate a new instance of *MyCppClass* when we
instantiate *WrapperClass*.

{% highlight python  %}
cdef class WrapperClass:
    cdef MyCppClass* C_Class

    def __cinit__(self):
        self.C_Class = new MyCppClass()
    def __dealloc__(self):
        del self.C_Class
{% endhighlight %}

Once we allow for instantiation of the class from python, we can define all
sorts of member functions and attributes __*just as we would for a standard
python class*__. So we can define the __\_\_init\_\___ function to set up some
attributes with a value at the time of instantiation (we'll get to
*self.Mydouble*, I promise).

{% highlight python  %}
def __init__(self, value):
    self.Mydouble = value
{% endhighlight %}


That's the boring part though. Here's the magic. We can define a python-style
function (note the *def* and not *cdef*) which casts the input to the appropriate
 c-type and then calls the *C++ level function* of our choice. I have examples
here of a function that returns a double and a void function. Additionally, we
can just use regular python here if we wish (for functions which don't need to be sped up by C++).

{% highlight python %}
def func(self, x, i):        
    cdef double c_x = x
    cdef int    c_i = i
    val = self.C_Class.cpp_func(c_x, c_i)
    return val

def void_func(self):
    self.C_Class.cpp_void_func()

def python_function(self, x, y):
    return x == y  
{% endhighlight %}

###   Define properties, allows for setting/getting them in python            
If you jumped the gun and tried to do this already, you might have noticed that
you don't have access to the C++ variables directly from python. This is because
 we're defining a wrapper class, whos attributes are only the ones we define
within the scope of *WrapperClass*. If we want to have read/write access to the
C++ level variables, we can use the python property function to do what we want.

Just define a function to set the C++ level variable and another one to get it
like so:

{% highlight python  %}
def get_cpp_double(self):
    return self.C_Class.cpp_double

def set_cpp_double(self, value):
    cdef double val = value
    self.C_Class.cpp_double = val
{% endhighlight %}

And the property function takes care of the rest:

{% highlight python  %}
Mydouble = property(get_cpp_double, set_cpp_double)
{% endhighlight %}

So now we have an attribute of *WrapperClass* called *Mydouble*. However,
*Mydouble* is basically an alias for the C++ level attribute *cpp_double*. If
you want to use the same names for C++ and Python variables, see the guide
[here](http://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#resolve-conflicts)
, but I'll just use different names for now.

Once the property defined in the .pyx file, you can use it within the wrapper
class as though it were a python variable (see *self.Mydouble* in \_\_init\_\_).

# 3) Compile

The easiest way to compile our Cython code is to use *distutils* and *cythonize*
in a python script. Simply include all the source files and make sure the
compiler knows to use C++.  

## Setup.py
{% highlight python  %}
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles  = ['ClassWrapper.pyx', 'Class.cpp']
compile_opts = ['-std=c++11']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++')]

setup(
  ext_modules=cythonize(ext)
)
{% endhighlight %}

To compile just run:
{% highlight python %}
python setup.py build_ext --inplace
{% endhighlight %}

in the directory with all the files. I essentially use the same setup file for
all of my projects.

# 4) Import and use

Whew! That was tiresome. Now we get to reap the rewards of all the hard work!
Once we run *setup.py* and compile our code, we should get a shared object file,
*ClassWrapper.so*. We can now import this just like any other python module. We
then have access to the class from the python level.

We can instantiate the class, and set the value of *self.Mydouble* to anything
that can be cast to a double:


{% highlight python  %}
import ClassWrapper
instance = ClassWrapper.WrapperClass(5)
print instance.Mydouble
{% endhighlight %}
{% highlight python  %}
>>> 5.0
{% endhighlight %}
We have read/write access via the *set_cpp_double* and *get_cpp_double*
functions which we call thusly:

{% highlight python  %}
instance.Mydouble = 34.5  #setter
print instance.Mydouble   #getter
{% endhighlight %}

{% highlight python  %}
>>> 34.5
{% endhighlight %}

We can call a void function, which changes the value of the C++ attribute
*cpp_double*. Since we wrapped this variable with the python level property
*Mydouble*, calling this function changes the value of *Mydouble*.

{% highlight python  %}
instance.void_func()
print instance.Mydouble
{% endhighlight %}

{% highlight python  %}
>>> 1.2
{% endhighlight %}


We can also call functions that take and return values, like this silly
implementation of multiplication:


{% highlight python  %}
print instance.func(3.5, 10)
{% endhighlight %}

{% highlight python  %}
>>> 35.0
{% endhighlight %}


And if we try to use the wrong variable type, we get an exception:


{% highlight python  %}
print instance.func('Wrongtype!', 2)
{% endhighlight %}


{% highlight python  %}
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-5-aa4d173bd403> in <module>()
----> 1 print instance.func('Wrongtype!', 2)


./ClassWrapper.pyx in ClassWrapper.WrapperClass.func (ClassWrapper.cpp:1057)()
     30
     31     def func(self, x, i):
---> 32         cdef double c_x = x
     33         cdef int    c_i = i
     34         val = self.C_Class.cpp_func(x, i)


TypeError: a float is required
{% endhighlight %}


And finally, you get an exception if you try to use a variable that's not a property in
*WrapperClass*, even though it's declared *public*.

{% highlight python  %}
instance.cpp_public
{% endhighlight %}


{% highlight python  %}
---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-6-a6bc21d6fa3e> in <module>()
----> 1 instance.cpp_public


AttributeError: 'ClassWrapper.WrapperClass' object has no attribute 'cpp_public'
{% endhighlight %}


# Conclusion

So, we went through how to wrap a C++ class in python using Cython. I really like being
able to selectively optimize various function as needed. This allows me to use
python when I want to, and C++ only when I need to (I may be a bit biased towards
 python, but so is any sane person).

Now I am aware that Cython offers functionality of defining c-level functions
within the .pyx files, and many of these can match the speed of optimized C++
code. However, I find it a bit easier to just wrap C++ directly, since I know
that I'm getting the best speed and don't have to worry about the nuances of
Cython (I think it's easier to write fast C++ code than it is to write fast
Cython code, particularly for more complex functions). Additionally, If you
already have C++ code lying around, you don't have to rewrite anything!
