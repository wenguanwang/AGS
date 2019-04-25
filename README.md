Caffe Implementation (v1) for

#Learning Unsupervised Video Primary Object Segmentation through Visual Attention (CVPR19)

[Wenguan Wang](https://sites.google.com/site/wenguanwangwwg/), Hongmei Song, Shuyang Zhao, Jianbing Shen, Sanyuan Zhao, Steven Chu Hong Hoi,  and Haibin Ling
- - -

1. Please install our modified [caffe](https://github.com/maysina/PDB-ConvLSTM/blob/master/maycaffe-convlstm.rar) first. 

2. Download the model weight from https://drive.google.com/open?id=1aO2nAaQMy-A76NjRSQDTx53AfpqyWUCt and put dvap_agos.caffemodel into the 'model' folder.
 
3. Then edit paths in './test/test.py' and './test/davis_bs3.txt'.

4. After you get the original results from the network, you can use './test/davis_crf.py' to process them.

5. Our results on DAVIS16, FBMS and Youtube can be find at 'seg_results.rar'.

6. Human eye fixation data for DAVIS16, Youtube and Segtrackv2 can be found at https://drive.google.com/open?id=11LAg69lnCp7TfWFYjntPm4RK4KfgL8_Y.

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

========================================================================

Any comments, please email: wenguanwang.ai@gmail.com
