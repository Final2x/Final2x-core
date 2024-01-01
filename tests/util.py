import json
import math
import os
from pathlib import Path

import cv2
import numpy as np
from Final2x_core.src.utils.getConfig import SRCONFIG
from skimage.metrics import structural_similarity

projectPATH = Path(__file__).resolve().parent.parent.absolute()

_GPUID_ = 0
# gpuid = -1 when in GitHub Actions
if os.environ.get("GITHUB_ACTIONS") == "true":
    _GPUID_ = -1


def load_image() -> np.ndarray:
    if CONFIG()[0] == -1:
        test_img = str(projectPATH / "assets" / "cpu-test.jpg")
    else:
        test_img = str(projectPATH / "assets" / "herta.jpg")

    img = cv2.imdecode(np.fromfile(test_img, dtype=np.uint8), cv2.IMREAD_COLOR)
    return img


def CONFIG() -> tuple[int, str, str, str]:
    gpuid = _GPUID_

    p_dict = {
        "gpuid": gpuid,
        "inputpath": [
            "./1/1/4/5/1/4/1/9/1/9/8/1/0.jpg",
            str(projectPATH / "assets" / "gray.jpg"),
            str(projectPATH / "assets" / "herta.jpg"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-20.png"),
            str(projectPATH / "assets" / "final2x-40.png"),
            str(projectPATH / "assets" / "final2x-80.png"),
            str(projectPATH / "assets" / "final2x-160.png"),
            str(projectPATH / "assets" / "final2x-320.png"),
            str(projectPATH / "assets" / "herta-unix-pic.exe"),
            str(projectPATH / "assets" / "vulkan-1.dll"),
        ],
        "model": "RealCUGAN-pro",
        "modelscale": 2,
        "modelnoise": 1,
        "outputpath": str(projectPATH / "assets"),
        "targetscale": 2,
        "tta": False,
    }

    p_json: str = json.dumps(p_dict)

    p_model: str = str(projectPATH / "src/Final2x_core/models")
    p_yaml = str(projectPATH / "src/Final2x_core/config.yaml")

    return gpuid, p_json, p_yaml, p_model


def getSRCONFIG() -> SRCONFIG:
    config = SRCONFIG()
    config.getConfigfromJson(CONFIG()[1], CONFIG()[3])
    return config


def calculate_image_similarity(image1: np.ndarray, image2: np.ndarray) -> bool:
    """
    calculate image similarity, check SR is correct
    :param image1: original image
    :param image2: upscale image
    :return:
    """
    # Resize the two images to the same size
    height, width = image1.shape[:2]
    image2 = cv2.resize(image2, (width, height))
    # Convert the images to grayscale
    grayscale_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    grayscale_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # Calculate the Structural Similarity Index (SSIM) between the two images
    (score, diff) = structural_similarity(grayscale_image1, grayscale_image2, full=True)
    print("img1.shape: ", image1.shape)
    print("img2.shape: ", image2.shape)
    print("SSIM: {}".format(score))
    return score > 0.8


def compare_image_size(image1: np.ndarray, image2: np.ndarray, t: float) -> bool:
    """
    compare original image size and upscale image size, check targetscale is correct
    :param image1: original image
    :param image2: upscale image
    :param t: targetscale
    :return:
    """
    target_size = (math.ceil(image1.shape[1] * t), math.ceil(image1.shape[0] * t))

    return image2.shape[0] == target_size[0] and image2.shape[1] == target_size[1]
