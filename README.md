# PAC-HP

This is the PyTorch version repo for [Precise Augmentation and Counting of Helicobacter Pylori in Histology Image](https://cyxhello.github.io/HPCDataset/) in NeurIPS 2022 workshop, which study the precise counting of Helicobacter Pylori (HP).

## Datasets
HP counting corpus HPCDataset [url](https://cyxhello.github.io/HPCDataset/): [Google Drive](https://drive.google.com/drive/folders/1f6cNEdAlltVXENQtn7DAaDrVOBW2xvrQ?usp=sharing)

## HP Generation

1. Get into the Generative model directory.
```bash
cd DCGAN/
```

2. Run DCGAN to generate single HP images.
```bash
python image_generation.py input.yaml
```

Parameters and input/output paths are passed through a _.yaml_ file. An example of all flags is stated below:

```
arch: 'DCGAN'

path: '/path/to/images/'
out: '/path/to/output/images'
run: 'name'
seed: 95
n_gpu: 1

num_epochs: 200
learning_rate: 0.0001
beta_adam: 0.5
batch_size: 8


latent_vector: 64

image_size: 64
loader_workers: 2
number_channels: 3
gen_feature_maps: 64
dis_feature_maps: 64
```

## Expert knowledge guided HP placement

1. Get into the synthetic directory.
```bash
cd synthetic/
```

2. Prepare the data
```bash
single/: single hp images generated by DCGAN.
single_clear/: single hp images with background noise removed
images/: real data.
```

3. image blending
```bash
python place_random.py
```

## HP Counting

1. Ground Truth

Please follow the `make_dataset.ipynb ` to generate the ground truth. It shall take some time to generate the dynamic ground truth. Note you need to generate your own json file.

2. Density Map

Generating the density map with a Gaussian kernel.

```bash
python gen_density.py
```

3. Training

```bash
python train.py train.json test.json 0 0
```

4. Testing
Follow the `val.ipynb` to try the validation. You can try to modify the notebook and see the output of each image.


