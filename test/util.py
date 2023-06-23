import cv2
import numpy as np
import json
from pathlib import Path
from skimage.metrics import structural_similarity

from src.utils.getConfig import SRCONFIG


def load_image() -> np.ndarray:
    try:
        img = cv2.imdecode(np.fromfile("./test/imgs/herta.jpg", dtype=np.uint8),
                           cv2.IMREAD_COLOR)
    except Exception:
        img = cv2.imdecode(np.fromfile("./imgs/herta.jpg", dtype=np.uint8),
                           cv2.IMREAD_COLOR)
    return img


def CONFIG() -> tuple[int, str, str, str]:
    projectPATH = Path(__file__).resolve().parent.parent.absolute()

    gpuid: int = 0  # -1 for CPU, > 0 for GPU
    p_dict = {
        "gpuid"      : gpuid,
        "inputpath"  : [
            "./1/1/4/5/1/4/1/9/1/9/8/1/0.jpg",
            str(projectPATH / "test" / "imgs" / "herta.jpg"),
            str(projectPATH / "test" / "imgs" / "herta.jpg"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-20.png"),
            str(projectPATH / "assets" / "final2x-40.png"),
            str(projectPATH / "assets" / "final2x-80.png"),
            str(projectPATH / "assets" / "final2x-160.png"),
            str(projectPATH / "assets" / "final2x-320.png"),
            str(projectPATH / "assets" / "final2x-640.png"),
            str(projectPATH / "assets" / "final2x-1280.png"),
        ],
        "model"      : "RealCUGAN-pro",
        "modelscale" : 2,
        "modelnoise" : 1,
        "outputpath" : str(projectPATH / "assets"),
        "targetscale": 2,
        "tta"        : True
    }

    p_json: str = json.dumps(p_dict)

    p_model: str = str(projectPATH / "models")
    p_yaml = str(projectPATH / "config.yaml")

    return gpuid, p_json, p_yaml, p_model


def getSRCONFIG() -> SRCONFIG:
    config = SRCONFIG()
    config.getConfigfromJson(CONFIG()[1], CONFIG()[3])
    return config


def calculate_image_similarity(image1: np.ndarray, image2: np.ndarray) -> bool:
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
