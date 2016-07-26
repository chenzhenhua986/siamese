import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array
import numpy as np
import math
import sys

# compute distance based on longitude and latitude
def dis(f1, f2):
  d = []
  for i in xrange(0, len(f1)):
     tmp = np.linalg.norm(np.array(f1[i])-np.array(f2[i]))
     print tmp
  
  d.append(tmp)
  return d

f1=[]
f2=[]

lmdb_env = lmdb.open('/l/vision/v5/chen478/siamese/d1')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    data = caffe.io.datum_to_array(datum)
    tmp=[]
    for i in xrange(0, len(data)):
      tmp.extend(data[i][0])
    f1.append(tmp)

print f1
lmdb_env = lmdb.open('/l/vision/v5/chen478/siamese/d2')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    data = caffe.io.datum_to_array(datum)
    tmp=[]
    for i in xrange(0, len(data)):
      tmp.extend(data[i][0])
    f2.append(tmp)

print f2
lmdb_env.close

print dis(f1, f2)



