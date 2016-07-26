#!/bin/bash

TOOLS=~/caffe/build/tools

export HDF5_DISABLE_VERSION_CHECK=1
export PYTHONPATH=/u/chen478/anaconda/lib/python2.7/site-packages:/u/chen478/caffe/python:/l/vision/v5/chen478/siamese
#for debugging python layer
GLOG_logtostderr=1  $TOOLS/caffe train -solver solver.prototxt -gpu 1
echo "Done."
