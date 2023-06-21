import cv2
import numpy as np
import pytest
import os
import pathlib
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


def getPath() -> tuple[str, str]:
    projectPATH = pathlib.Path(os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    p_yaml = str(projectPATH / "config.yaml")
    p_model = str(projectPATH / "models")
    return p_yaml, p_model


def calculate_image_similarity(image1: np.ndarray, image2: np.ndarray) -> bool:
    # Resize the two images to the same size
    height, width = image1.shape[:2]
    image2 = cv2.resize(image2, (width, height))
    # Convert the images to grayscale
    grayscale_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    grayscale_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # Calculate the Structural Similarity Index (SSIM) between the two images
    (score, diff) = structural_similarity(grayscale_image1, grayscale_image2, full=True)
    print("SSIM: {}".format(score))
    return score > 0.8


class Test_SRBaseClass:
    def test_init_error(self):
        from src.SRFactory.SRBaseClass import SRBaseClass
        with pytest.raises(TypeError):
            _ = SRBaseClass()


class Test_REALCUGAN:
    def test_case_RealCUGAN_pro(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfig(getPath()[0], getPath()[1])
        config.model = "RealCUGAN-pro"
        SR = REALCUGAN()
        img1 = load_image()
        img2 = SR.process(img1)
        print("img1.shape: ", img1.shape)
        print("img2.shape: ", img2.shape)
        assert calculate_image_similarity(img1, img2)

    def test_case_RealCUGAN_se(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfig(getPath()[0], getPath()[1])
        config.model = "RealCUGAN-se"
        SR = REALCUGAN()
        img1 = load_image()
        img2 = SR.process(img1)
        print("img1.shape: ", img1.shape)
        print("img2.shape: ", img2.shape)
        assert calculate_image_similarity(img1, img2)


class Test_REALESSRGAN:
    def test_case_1(self):
        from src.SRFactory import REALESRGAN
        config = SRCONFIG()
        config.getConfig(getPath()[0], getPath()[1])
        SR = REALESRGAN()
        img1 = load_image()
        img2 = SR.process(img1)
        print("img1.shape: ", img1.shape)
        print("img2.shape: ", img2.shape)
        assert calculate_image_similarity(img1, img2)
