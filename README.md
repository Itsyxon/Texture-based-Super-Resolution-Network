# The Unreasonable Effectiveness of Texture Transfer for Single Image Super-resolution.

This is the pytorch implementation of Texture based Super Resolution Networks (TSRN) presented in the paper [The Unreasonable Effectiveness of Texture Transfer for Single Image Super-resolution](https://arxiv.org/abs/1808.00043). The code is tested on Pytorch > v0.4 with python 3.5.

If you use this work then cite us.

```
@inproceedings{waleed2018unreasonable,
  title={The unreasonable effectiveness of texture transfer for single image super-resolution},
  author={Waleed Gondal, Muhammad and Scholkopf, Bernhard and Hirsch, Michael},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  pages={0--0},
  year={2018}
}
```

## Prerequisite

Install pytorch and torchvision
first from the official [website](http://pytorch.org/). You can use the following command to install the latest version for python 3.5.

```
pip3 install torch torchvision
```

## Dataset

For training the semantically guided TSRN models, we used MS-COCO Stuff dataset. Semantically annotated dataset can be downloaded from this [website](http://cocodataset.org/#download).

## Training

Two different training configurations are provided for TSRN-global and TSRN-segmented. To train a `TSRN-Global` model provide path to root directory and set upscale factor accordingly

```
python train.py --upscale_factor 8 --cropsize 256 --path_data '/home/mscoco/train2017'

```

To train a `TSRN-Segmented` model provide additional path to annotation files for semantic segmentation.

```
python train_segmented.py --upscale_factor 4 --cropsize 256 --path_data '/home/mscoco/train2017' --annFile '/home/coco_stuff/stuff_train2017.json'

```

The weights and sample super-resolved images are saved at each epoch in the trainings folder.

## Testing

Pretrained models of TSRN-S and TSRN-G for both 4x and 8x SISR are provided in the resources folder. The models should be able to run on both CPU and GPU. To test a model, provide path to the
test images, the upscaling factor and the corresponding path to the pretrained weights.

```
python test.py --upscale_factor 4 --path_model './resources/pretrained/tsrn_global_4x.pth' --path_data './resources/images'

```

## Start

```
docker build . -t dl-test

```

```
docker run --name dl-test -d -i -t dl-test /bin/sh

```

```
docker exec -t -i dl-test /bin/bash

```

```
python train.py --upscale_factor 8 --cropsize 256 --path_data 'src/datasets'

```

## Testing images

```
cd src/test

```

```
python tbsr-test.py

```
