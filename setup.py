# run with
# python setup.py build_ext --inplace

nrn_srcdir = "."
instdir = "/home/debora/neuron/nrn"
if nrn_srcdir[0] != '/' :
    # TODO: is this right?
    nrn_srcdir = '../../../../../../' + nrn_srcdir

from distutils.core import setup
from distutils.extension import Extension
try:
    import numpy
except:
    setup()
else:
    mpicc_bin = "gcc"
    mpicxx_bin = "g++"
    import os
    os.environ["CC"]=mpicc_bin
    os.environ["CXX"]=mpicxx_bin

    include_dirs = [nrn_srcdir + '/share/lib/python/neuron/rxd/geometry3d', '.', numpy.get_include()]

    srcdir = nrn_srcdir + '/share/lib/python/neuron/rxd/geometry3d/'

    #    name='neuron/rxd/geometry3d',
    setup(
        ext_modules = [
                       Extension("graphicsPrimitives",
                                 sources=["graphicsPrimitives.cpp"],
                                 include_dirs=include_dirs),
                       Extension("ctng",
                                 sources=["ctng.cpp"],
                                 include_dirs=include_dirs),
                       Extension("surfaces",
                                 sources=["surfaces.cpp", srcdir + "marching_cubes2.c", srcdir + "llgramarea.c"],
                                 include_dirs=include_dirs)],
    )
    #    package_dir = {'': instdir + '/share/lib/python/neuron/rxd/geometry3d'}

