Caffe Implementation (v1) for

[Learning Unsupervised Video Object Segmentation through Visual Attention (CVPR19)](https://www.researchgate.net/publication/332751903_Learning_Unsupervised_Video_Object_Segmentation_through_Visual_Attention)

[Paying Attention to Video Object Pattern Understanding (PAMI20)](https://www.researchgate.net/publication/338528322_Paying_Attention_to_Video_Object_Pattern_Understanding)
- - -

===========================================================================

## :fire::fire::fire:Update

2019/10: Results on DAVIS17 val and test sets are added (instance-level video object segmentation)

===========================================================================

1. Please install our modified [caffe](https://github.com/maysina/PDB-ConvLSTM/blob/master/maycaffe-convlstm.rar) first. 

2. Download the model weight from https://drive.google.com/open?id=1aO2nAaQMy-A76NjRSQDTx53AfpqyWUCt and put dvap_agos.caffemodel into the 'model' folder.
 
3. Then edit paths in './test/test.py' and './test/davis_bs3.txt'.

4. After you get the original results from the network, you can use './test/davis_crf.py' to process them.

5. Our results on DAVIS16, FBMS and Youtube can be find at 'seg_results.rar'. Saliency results can be found at https://drive.google.com/file/d/1qtr2h69MEkBYLno_KqYIuiwZGFYmSHr4/view?usp=sharing

6. Human eye fixation data for DAVIS16, Youtube and Segtrackv2 can be found at https://drive.google.com/open?id=11LAg69lnCp7TfWFYjntPm4RK4KfgL8_Y.

7. Our model, segmentation and saliency results, and fixation data can also be found at Baidu Pan
https://pan.baidu.com/s/1hz6iVOAMW3QRORebK3mC3Q , extaction code: 6prn 


If you find our project helpful, your citations are highly appreciated:

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

Other related projects/papers:

[Zero-shot Video Object Segmentation via Attentive Graph Neural Networks (ICCV2019 Oral)](https://github.com/carrierlxk/AGNN)

[See More, Know More: Unsupervised Video Object Segmentation With Co-Attention Siamese Networks (CVPR19)](https://github.com/carrierlxk/COSNet) 

[Saliency-Aware Geodesic Video Object Segmentation (CVPR15)](https://github.com/wenguanwang/saliencysegment)





========================================================================
This repository is no longer maintained. 
