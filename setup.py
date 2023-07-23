# -------------------------------------------------------------------
# Copyright (C) 2020 Università degli studi di Milano-Bicocca, iralab
# Author: Daniele Cattaneo (d.cattaneo10@campus.unimib.it)
# Released under Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-nc-sa/4.0/
# -------------------------------------------------------------------
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ['-std=c++14']

nvcc_args = [
    # '-gencode', 'arch=compute_50,code=sm_50',
    # '-gencode', 'arch=compute_52,code=sm_52',
    # '-gencode', 'arch=compute_60,code=sm_60',
    # '-gencode', 'arch=compute_61,code=sm_61',
    # '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_70,code=compute_70',
    '-gencode', 'arch=compute_75,code=compute_75',
    '-gencode', 'arch=compute_86,code=compute_86'
]

setup(
    name='visibility',
    version='0.1',
    author="Daniele Cattaneo",
    author_email="cattaneo@informatik.uni-freiburg.de",
    url="https://github.com/catta202000/CMRNet",
    ext_modules=[
        CUDAExtension('visibility', [
            'src/visibility.cpp',
            'src/visibility_kernel.cu',
        ], extra_compile_args={'cxx': cxx_args, 'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
