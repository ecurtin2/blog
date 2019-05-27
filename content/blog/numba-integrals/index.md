---
title: Use Numba for fast integrals
date: 2016-12-14
tags: ["Python", "math"]
author: Evan Curtin
description: C speed from python.
---

Here's a quick tip to make your integrals super fast in python. Suppose you wanted to integrate a function in 3D. We can start by import nquad from scipy and defining our function.


```python
from scipy.integrate import nquad
from math import sqrt, exp, sin, cos

def f(x, y, z):
    return sin(cos(sqrt(exp(x)**2 + exp(y)**2 + exp(z)**2)))
```

nquad makes it super easy to integrate a function in any number of dimensions, lets see:


```python
ranges=((1, 2), (1, 2), (1, 2))
nquad(f, ranges)
```




    (-0.14048187566074577, 1.4506979457578973e-08)



Let's check how long it took:


```python
%timeit nquad(f, ranges)
```

    19.5 ms ± 222 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


Pretty good, right? Well let's see if we can do better (because maybe with a different function we'll need to). [Numba](https://numba.pydata.org/) is a just-in-time compiler focused on numeric python. Let's give it a try:


```python
import numba
```

It works by adding a @jit decorator to our function. It infers the types of the arguments when it sees them and compiles the function into LLVM bytecode. The result can be significantly faster (I've seen easily two orders of magnitude). 


```python
@numba.jit
def f(x, y, z):
    return sin(cos(sqrt(exp(x)**2 + exp(y)**2 + exp(z)**2)))
```

Let's see if it's still correct and how long it takes:


```python
print(nquad(f, ranges))
%timeit nquad(f, ranges)
```

    (-0.14048187566074577, 1.4506979457578973e-08)
    10.9 ms ± 17.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


Hey! Twice as fast with no work at all! Pretty nice if you ask me. But there is one more layer. The nquad function calls our compiled function from python, meaning that every time it calls the function we're getting python function call overhead. Fortunately, scipy now has support for  *LowLevelCallable* types. The specifics are in the documentation, but basically you can use a c function from scipy and the nquad routine will call it directly, without indirection to the python interpreter. 


```python
from scipy import LowLevelCallable
```

I never particularly cared for this, until I also saw that Numba now supports generating c functions directly from Python! Scipy needs a c-level function with the signature `double(int, double*)`, so we have to tell numba this is what we want. This is very easy. Unfortunately, this also means we are a bit more restricted in what we can do here. 


```python
from numba import cfunc, types, carray

c_sig = types.double(types.intc, types.CPointer(types.double))
@cfunc(c_sig)
def f(n, data):
    total = 0.0
    for i in range(n):
        total += exp(data[i])**2
    return sin(cos(sqrt(total)))
```


```python
new_f = LowLevelCallable(f.ctypes)
print(nquad(new_f, ranges))
%timeit nquad(new_f, ranges)
```

    (-0.14048187566074577, 1.4506979457578973e-08)
    6.2 ms ± 14.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


Cool! We beat the straightforward numba approach. Unfortunately we had to write a little bit more c-like code. It's not too bad though. I'm betting we can also take advantage of how Numba basically inlines variables it knows at compile time to do basically whatever we want. The cool thing here is that we're calling QUADPACK with a C level callback function, and the performance should be essentially optimal, as the python overhead is minimized. 
