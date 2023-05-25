# HP COUNTING

## Prerequisites
We strongly recommend Anaconda as the environment.

Python: 2.7

PyTorch: 0.4.0

CUDA: 9.2

## Data Preprocessing

1. Ground Truth

Please follow the `make_dataset.ipynb ` to generate the ground truth. It shall take some time to generate the dynamic ground truth. Note you need to generate your own json file.

2. Density Map

Generating the density map with a Gaussian kernel.

```bash
python gen_density.py
```

## Training 

Try `python train.py train.json test.json 0 0` to start training process.




源训练集，源测试集
```bash
nohup python train.py train.json test.json 0 0 > crowd_ori.log &
```

合成训练集，源测试集
```bash
nohup python train.py single_4_train.json test.json 1 1 > single.log &
```

混合训练集，源测试集
```bash
nohup python train_normal.py normal_blending.json test.json 2 2 > blending.log &
```


## Testing
Follow the `val.ipynb` to try the validation. You can try to modify the notebook and see the output of each image.


## References
ShanghaiA MAE: 66.4 [Google Drive](https://drive.google.com/open?id=1Z-atzS5Y2pOd-nEWqZRVBDMYJDreGWHH)
ShanghaiB MAE: 10.6 [Google Drive](https://drive.google.com/open?id=1zKn6YlLW3Z9ocgPbP99oz7r2nC7_TBXK)

CSRNET
```
@inproceedings{li2018csrnet,
  title={CSRNet: Dilated convolutional neural networks for understanding the highly congested scenes},
  author={Li, Yuhong and Zhang, Xiaofan and Chen, Deming},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={1091--1100},
  year={2018}
}
```


```
@inproceedings{zhang2016single,
  title={Single-image crowd counting via multi-column convolutional neural network},
  author={Zhang, Yingying and Zhou, Desen and Chen, Siqin and Gao, Shenghua and Ma, Yi},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={589--597},
  year={2016}
}
```
