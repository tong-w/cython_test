from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "math_wrapper",
        sources=["wrapper.pyx"],
        include_dirs=["./cpp"],  # 头文件路径
        language="c++",
        extra_compile_args=["-std=c++11"],  # C++ 标准
    )
]

setup(
    name="math_wrapper",
    ext_modules=cythonize(extensions),
)