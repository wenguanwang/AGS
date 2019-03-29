Caffe Implementation (v1) for

#Learning Unsupervised Video Primary Object Segmentation through Visual Attention (CVPR19)
- - -

1. Please install our modified [caffe](https://github.com/maysina/PDB-ConvLSTM/blob/master/maycaffe-convlstm.rar) first. 

2. Then edit paths in './test/test.py' and './test/davis_bs3.txt'.

3. After you get the original results from the network, you can use './test/davis_crf.py' to process them.

4. In order to get the binary map, you can run the './test/binary.m' after get the results with crf.

If you find our method useful in your research, please cite the following papers:


@InProceedings{Wang_2019_CVPR,
author = {Wang, Wenguan and Song, Hongmei and Zhao, Shuyang and Shen, Jianbing and Zhao, Sanyuan and Hoi, Steven Chu Hong and Ling, Haibin},
title = {Learning Unsupervised Video Object Segmentation through Visual Attention},
booktitle = {CVPR},
year = {2019}
}



@InProceedings{Song_2018_ECCV,
author = {Song, Hongmei and Wang, Wenguan and Zhao, Sanyuan and Shen, Jianbing and Lam, Kin-Man},
title = {Pyramid Dilated Deeper ConvLSTM for Video Salient Object Detection},
booktitle = {ECCV},
year = {2018}
}


