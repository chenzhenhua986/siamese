export PYTHONPATH=/u/chen478/anaconda/lib/python2.7/site-packages:/u/chen478/caffe/python:/l/vision/v5/chen478/siamese
~/caffe/build/tools/extract_features.bin  /l/vision/v5/chen478/siamese/siamese_iter_100.caffemodel  deploy.prototxt deconv1 d1 30 lmdb GPU 1
~/caffe/build/tools/extract_features.bin  /l/vision/v5/chen478/siamese/siamese_iter_100.caffemodel  deploy.prototxt deconv1_p d2 30 lmdb GPU 1
echo 'done'
