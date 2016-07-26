import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array
import numpy as np
import matplotlib.image as mpimg
import Image

lmdb_env = lmdb.open('/l/vision/v5/chen478/siamese/d1')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

j=0
for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    feat = caffe.io.datum_to_array(datum)

    print 'Processing part one, image: ' + str(j)
    feat = (((feat - feat.min()) / (feat.max() - feat.min()))*255.9).astype(np.uint8)
#    mpimg.imsave("part1_" + str(j) + ".png", feat)
    img = Image.fromarray(feat[0])
    img.save("part1_" + str(j) + ".png")
    j += 1

lmdb_env = lmdb.open('/l/vision/v5/chen478/siamese/d2')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

j=0
for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    feat = caffe.io.datum_to_array(datum)

    print 'Processing part two, image: ' + str(j)
    feat = (((feat - feat.min()) / (feat.max() - feat.min()))*255.9).astype(np.uint8)
    img = Image.fromarray(feat[0])
    img.save("part2_" + str(j) + ".png")
    j += 1

