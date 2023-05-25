
# DCGAN

A DCGAN is a specific flavor of GAN dedicated to image generation. The architecture consists on a _Generator_ and a _Discriminator_ built upon four 2d convolutional layers. The _Discriminator_ in build out of strided convolutions, batch normalization layers and uses Leaky Relu activations. Originally, the input size of the images is 64 and it is already set to process color images (3x64x64). The _Generator_ differs from the _Discriminator_ in the convolutional layers, which are transposed. It has as an input a random vector sampled from a normal distribution which will be transformed by adversarial training into an RGB image of the selected shape.

## 128x128 & 256x256 image generation

For our final goal, specific class balancing, we needed to generate images of the proper size. The original DCGAN implementation creates images of size 64x64, but our classificator, which is built using an EfficientNet works with input size of 128x128. Furthermore we were interested in creating even bigger images, of 256x256, and assess the quality of those. Thus, in this repository we modified the original architecture and for both DCGAN and SNGAN for generating bigger images. 

## Metrics

### Bar of measures

Measure | Bar | 
:------: | :------:|
PSNR   | Context dependant, generally the higher the better.      | 
SSIM   |  Ranges from 0 to 1, being 1 the best value.     | 
MS-GMSD |  Ranges from 0 to 1, being 1 the best value.    |  
MDSI   |   Ranges from 0 to inf, being 0 the best value.    |
HaarPSI |   Ranges from 0 to 1, being 1 the best value.   |


## Execution

Run DCGAN to generate single HP images.
```bash
python image_generation.py input.yaml
```
### Parameters

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

