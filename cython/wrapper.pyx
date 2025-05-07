# distutils: language = c++
# distutils: sources = ./cpp/math_functions.cpp

from libcpp cimport bool

cdef extern from "./cpp/math_functions.h" namespace "cppmath":
    double square(double x)
    int fib(int n)

def py_square(double x):
    return square(x)

def py_fib(int n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return fib(n)