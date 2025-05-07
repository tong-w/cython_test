# --- import
import math
import time
import sys
from tracemalloc import start

sys.path.append("cython")
import math_wrapper


# ---- code
def main():
    print("Hello from cython-test!")
    print("new message from b1")
    print("branch from main")

    print("message from b2 which splited from main branch")

    print("message from b2 which splited from main branch")

def fib(n):
    a, b =0, 1
    for _ in range(n):
        a,b = b,a+b
    return a


#  --- excute
if __name__ == "__main__":
    print(math_wrapper.py_square(2.5))
    print('-'*30)
    print(math_wrapper.py_fib(1000))
    print(math_wrapper.__file__)
    print('-'*30)
    start1 = time.time()
    fib(1000000)
    print(f"python time:{(time.time() - start1):.4F}")
    print('-'*30)
    start2 = time.time()
    math_wrapper.py_fib(1000000)
    print(f"cython time:{(time.time() - start2):.4F}")
    print('-'*30)






