---
title: HTML Reports
date: 2026-02-07
tags: ["Python"]
author: Evan Curtin
description: 

---
```python
import altair as alt
from jinja2 import Template
import json
import pandas as pd
```


```python
from vega_datasets import data
iris = data.iris()

cars = alt.Chart(iris, title="Iris Chart").mark_point().encode(
    x='petalLength',
    y='petalWidth',
    color='species'
).interactive()
```


```python
from typing import List, Optional

class EmbedChart:
    template = Template("""<div id="vis-{{ id }}"></div>
    <script type="text/javascript">
        var spec = {{ spec }};
        var opt = {"renderer": "canvas", "actions": false};
        vegaEmbed("#vis-{{ id }}", spec, opt);
    </script>
    """)
    current_id = 0
    def __init__(self, chart: alt.Chart):
        self.chart = chart
        self._id = __class__.current_id
        __class__.current_id += 1
        
    def __str__(self):
        spec = json.dumps(self.chart.to_dict(), indent=2)
        return __class__.template.render(spec=spec, id=self._id)
    
class EmbedFrame:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def __str__(self):
        return self.df._repr_html_()
        
from dataclasses import dataclass
        
@dataclass
class Section:
    title: str
    content: str
    tables: Optional[List[pd.DataFrame]]
    charts: Optional[List[alt.Chart]]
    current_id = 0
        
    template: Template = Template("""
    <div class="section" id="section-{{ id }}">
        <hr>
        <h2>{{ title }}</h2>
        {{ content }}
        {% for table in tables %}
            {{ table }}
        {% endfor %}
        {% for chart in charts %}
            {{ chart }}
        {% endfor %}
    </div>
    """)
        
    def __post_init__(self):
        self._id = __class__.current_id
        __class__.current_id += 1

    def __str__(self):
        charts = [EmbedChart(c) for c in self.charts]
        tables = [EmbedFrame(df) for df in self.tables]
        
        return __class__.template.render(title=self.title, content=self.content, tables=tables, charts=charts, id=self._id)
    

DEFAULT_CSS =  """
table { 
    width: 750px; 
    border-collapse: collapse; 
    margin:50px auto;
}

/* Zebra striping */
tr:nth-of-type(odd) { 
    background: #eee; 
}

th { 
    background: #3498db; 
    color: white; 
    font-weight: bold; 
}

td, th { 
    padding: 10px; 
    border: 1px solid #ccc; 
    text-align: left; 
    font-size: 18px;
}
"""

class Report:
    template = Template("""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
      
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mini.css/3.0.1/mini-default.min.css">
    <style>
    body {
        max-width: 700px;
        margin: auto;
    }
    </style>
    </head>
    <body>
    <main class="app-container">
        <article>
            <div id="toc_container">
            <h1 class="toc_title">Contents</h1>
            <ul class="toc_list">

            {% for section in sections %}
                <li><a href="#section-{{ section._id }}">{{ section.title }}</a></li>
            {% endfor %}

            </ul>
            </div>

            {% for section in sections %}
                {{ section }}
            {% endfor %}
        </article>
        </main>
    </body>
    </html>
    """)
    

    
    def __init__(self, sections: List[Section], css=DEFAULT_CSS):
        self.sections = sections
        self.css = css
        
    def __str__(self):
        return __class__.template.render(sections=self.sections, css=self.css)
    

```


```python
css_file = "/home/evan/projects/blog/static/Blogs __ Evan's Blog_files/main.min.465c4a0bba48be825ec830b7581563541c732256bcb5ecac4b90c41fd89c318d.css"

with open(css_file) as f:
    css = f.read()

secs = [Section(title=f"cars{i}", content="This is a cars section", tables=[iris.head()], charts=[cars]) for i in range(10)]

report = Report(sections=secs, css=css)

with open("test.html", "w") as f:
    f.write(str(report))
```


```python

```


```python

```


```python

```


```python

```


```python

```
