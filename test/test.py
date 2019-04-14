import numpy as np
import sys
sys.path.append('your_path/caffe/python')
import caffe
import os
import cv2
import scipy.misc as misc
import datetime
import math

def MaxMinNormalization(x,Max,Min):  
    x = (x - Min) / (Max - Min)
    return x

caffe.set_mode_gpu()
caffe.set_device(0)
print("Load net...")
net = caffe.Net('../model/deploy.prototxt', '../model/dvap_agos.caffemodel', caffe.TEST)

with open('./davis_bs3.txt') as f:
	lines = f.readlines()

for idx in range(len(lines)/3):
	print("Run net...")
	net.forward()
	for i in range(3):
		if ' 0' in lines[idx*3+i]:
			line = lines[idx*3+i].replace(" 0\n", "")
		else:
			line = lines[idx*3+i].replace(" 1\n", "")
		dir, file = os.path.split(line)
		file = file.replace(".jpg", '.png')
		video = dir.split("/")[-1]
		img = misc.imread(line)


		all1 = net.blobs['conv6_sm'].data
		out1 = all1[i][0]
		out1 = misc.imresize(out1, img.shape)
		out1 = out1.astype('float')
		out1 = MaxMinNormalization(out1, out1.max(), out1.min())
		savePath1 = './reults/davis/' + video + '/'
		if not os.path.exists(savePath1):
			os.makedirs(savePath1)
		misc.imsave(savePath1 + file, out1)
		print('Save the ' + str(idx*3+i) + ' Image: ' + savePath1 + file)

		# all2 = net.blobs['conv7_sm'].data
		# out2 = all2[i][0]
		# out2 = misc.imresize(out2, img.shape)
		# out2 = out2.astype('float')
		# out2 = MaxMinNormalization(out2, out2.max(), out2.min())
		# savePath2 = './results/davis_attention/'
		# if not os.path.exists(savePath2):
		# 	os.makedirs(savePath2)
		# misc.imsave(savePath2 + video + '_' + file, out2)
		# print('Save the ' + str(idx*3+i) + ' Image: ' + savePath2 + file)

print("Done!")		