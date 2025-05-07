#include "math_functions.h"

namespace cppmath{
    double square(double x ){
        return x*x;
    }

    int fib(int n)
    {
        int a =0, b=1;
        for ( int i = 0; i<n; ++i){
            int temp = a;
            a=b;
            b = temp+a;
        }
        return a;
    }
}