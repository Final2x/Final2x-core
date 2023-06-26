<p align="center">

<img src="https://s2.loli.net/2023/06/19/547qRecHdnJIbKu.png" height="128">

</p>

<h1 align="center"> Final2x-core </h1>

![MacOS arm64](https://img.shields.io/badge/Support-MacOS%20arm64-blue?logo=Apple&style=flat-square)
![MacOS x64](https://img.shields.io/badge/Support-MacOS%20x64-blue?logo=Apple&style=flat-square)
![Windows x64](https://img.shields.io/badge/Support-Windows%20x64-blue?logo=Windows&style=flat-square)
![Linux x64](https://img.shields.io/badge/Support-Linux%20x64-blue?logo=Linux&style=flat-square)
[![codecov](https://codecov.io/gh/Tohrusky/Final2x-core/branch/main/graph/badge.svg?token=B2TNKYN4O4)](https://codecov.io/gh/Tohrusky/Final2x-core) 
[![CI-test](https://github.com/Tohrusky/Final2x-core/actions/workflows/CI-test.yml/badge.svg)](https://github.com/Tohrusky/Final2x-core/actions/workflows/CI-test.yml) 
[![CI-build](https://github.com/Tohrusky/Final2x-core/actions/workflows/CI-build.yml/badge.svg)](https://github.com/Tohrusky/Final2x-core/actions/workflows/CI-build.yml)
[![Release](https://github.com/Tohrusky/Final2x-core/actions/workflows/Release.yml/badge.svg)](https://github.com/Tohrusky/Final2x-core/actions/workflows/Release.yml)
![GitHub](https://img.shields.io/github/license/Tohrusky/Final2x-core)


Final2x-core is a cross-platform image super-resolution CLI tool for [Final2x](https://github.com/Tohrusky/Final2x). 

# Use

```shell
usage: Final2x-core [-h] [-j JSON]

when -j is not specified, the config.yaml file in the directory will be read automatically

optional arguments:
  -h, --help            show this help message and exit
  -j JSON, --JSON JSON  JSON str for config

```

# Config

Pass the config json string to the program through the `-j` parameter.

**PLEASE NOTE: the config is JSON, remove the // comments before use.**

```
{
  "gpuid": 0, // GPU id, >= -1 (-1 for CPU, may not work for some models.)
  "inputpath": [
    // Input image paths, should be a list.
    "path/to/img1.jpg", 
    "path/to/img2.png"
  ],
  "model": "RealCUGAN-pro", // model name
  "modelscale": 2, // model upscale factor
  "modelnoise": -1, // DENOISE level
  "outputpath": "path/to/output", // output path
  "targetscale": 2.0, 
  // Target upscale factor, upscale multiple times to achieve the target upscale factor.
  // If not invalid, use modelscale.
  "tta": false // Test Time Augmentation, default false
}
```

**SUPPORTED MODEL LIST:**

- RealCUGAN-se:
    - model: "RealCUGAN-se"
    - scale: 2
        - noise: -1, 0, 1, 2, 3
    - scale: 3, 4
        - noise: -1, 0, 3

- RealCUGAN-pro:
    - model: "RealCUGAN-pro"
    - scale: 2, 3
    - noise: -1, 0, 3

- RealESRGAN-animevideov3:
    - gpuid : >= 0
    - model: "RealESRGAN-animevideov3"
    - scale: 2, 3, 4

- RealESRGAN:
    - gpuid : >= 0
    - model: "RealESRGAN"
    - scale: 4

- RealESRGAN-anime:
    - gpuid : >= 0
    - model: "RealESRGAN-anime"
    - scale: 4

- Waifu2x-cunet:
    - model: "Waifu2x-cunet"
    - scale: 1
        - noise: 0, 1, 2, 3
    - scale: 2
        - noise: -1, 0, 1, 2, 3

- Waifu2x-upconv_7_anime_style_art_rgb:
    - model: "Waifu2x-upconv_7_anime_style_art_rgb"
    - scale: 2
    - noise: -1, 0, 1, 2, 3

- Waifu2x-upconv_7_photo:
    - model: "Waifu2x-upconv_7_photo"
    - scale: 2
    - noise: -1, 0, 1, 2, 3

- SRMD:
    - gpuid : >= 0
    - model: "SRMD"
    - scale: 2, 3, 4
    - noise: -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Build

[Github Action](https://github.com/Tohrusky/Final2x-core/actions/workflows/CI-build.yml)

*The project just only been tested in Ubuntu 18+ and Debian 9+ environments on Linux, so if the project does not work on
your system, please try building it.*

# Reference

The following references were used in the development of this project:

[ncnn](https://github.com/Tencent/ncnn) - ncnn is a high-performance neural network inference framework developed by
Tencent AI Lab.

[nihui/realcugan-ncnn-vulkan](https://github.com/nihui/realcugan-ncnn-vulkan) - This project provided the core
implementation of the Real-CUGAN algorithm using the ncnn and Vulkan libraries.

[xinntao/Real-ESRGAN-ncnn-vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan) - This project provided the core
implementation of the Real-ESRGAN algorithm using the ncnn and Vulkan
libraries.

[nihui/waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan) - This project provided the core
implementation of the Waifu2x algorithm using the ncnn and Vulkan libraries.

[nihui/srmd-ncnn-vulkan](https://github.com/nihui/srmd-ncnn-vulkan) - This project provided the core implementation of
the SRMD algorithm using the ncnn and Vulkan libraries.

[realcugan-ncnn-py](https://github.com/Tohrusky/realcugan-ncnn-py) - This project provided the Python Binding for
realcugan-ncnn-vulkan with PyBind11

[realesrgan-ncnn-py](https://github.com/Tohrusky/realesrgan-ncnn-py) - This project provided the Python Binding for
realesrgan-ncnn-vulkan with PyBind11

[waifu2x-ncnn-py](https://github.com/Tohrusky/waifu2x-ncnn-py) - This project provided the Python Binding for
waifu2x-ncnn-vulkan with PyBind11

[srmd-ncnn-py](https://github.com/Tohrusky/srmd-ncnn-py) - This project provided the Python Binding for srmd-ncnn-vulkan
with PyBind11

# License

This project is licensed under the BSD 3-Clause - see
the [LICENSE file](https://github.com/Tohrusky/Final2x-core/blob/main/LICENSE) for details.
