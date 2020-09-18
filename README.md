# circum-cam

![build](https://travis-ci.com/LumineerLabs/circum-cam.svg?branch=master) ![PyPI](https://img.shields.io/pypi/v/circum-cam)

Webcam + ML sensor plugin for [circum](https://github.com/LumineerLabs/circum).

circum-cam uses a machine learning algorithm to identify and estimate the poses of people in an image. It takes a video 
stream from a webcam and periodically submits frames to the ML algorithm and reports the results to the circum network. 
Because it is able to identify detailed pose information, that is included for clients to utilize, if desired.

## Install

1. Install the circum-cam endpoint plugin.

```bash
pip3 install circum-cam
```

2. Download the pretrained [SMAP](https://github.com/LumineerLabs/circum-cam/raw/master/models/SMAP_model.pth) and 
[RefineNet](https://github.com/LumineerLabs/circum-cam/raw/master/models/RefineNet.pth) models. NOTE: these are 
distributed under the [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0#:~:text=%20Apache%20License%2C%20Version%202.0%20%201%20Definitions.%0A%22License%22,of%20this%20License%2C%20each%20Contributor%20hereby...%20More%20) 
please see https://github.com/LumineerLabs/circum-cam/raw/master/models/NOTICE, 
https://github.com/LumineerLabs/circum-cam/raw/master/models/LICENSE, and
https://choosealicense.com/licenses/apache-2.0/ for more details.

If those links don't work, try https://github.com/zju3dv/SMAP#run-inference-on-custom-images

## Usage

```bash
```

## References

circum-cam would not have been possible without the following references:

* Jianan Zhen, Qi Fang, Jiaming Sun, Wentao Liu, Wei Jiang, Hujun Bao, Xiaowei Zhou. 
[SMAP: Single-Shot Multi-Person Absolute 3D Pose Estimation](https://www.catalyzex.com/paper/arxiv:2008.11469)
* https://github.com/zju3dv/SMAP