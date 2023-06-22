from abc import ABC, abstractmethod
import numpy as np
import cv2
import math
from typing import final

from src.utils.getConfig import SRCONFIG


class SRBaseClass(ABC):
    def __init__(self):
        config = SRCONFIG()
        self._targetscale: float = config.targetscale  # user upscale factor
        self._gpuid: int = config.gpuid  # gpu id, -1 for cpu
        self._tta: bool = config.tta  # use tta
        self._model: str = config.model  # model name
        self._modelscale: int = config.modelscale  # model upscale factor
        self._modelnoise: int = config.modelnoise  # model noise level
        self._alphavalue: float = config.alphavalue  # alpha value for RealCUGAN

        self._sr_n = 1  # super-resolution times
        self._set_sr_n()

        self._SR_class = None  # upscale model, override in child class

        self._target_size: tuple[int, int] = (0, 0)  # target size of the image

        print("SRBaseClass init")

    @final
    def _set_sr_n(self) -> None:
        """
        set super-resolution times, when targetscale > modelscale
        :return:
        """
        s: int = self._modelscale
        while self._targetscale > s:
            self._sr_n += 1
            s *= self._modelscale
        print("sr_n set to", self._sr_n)

    @abstractmethod
    def _init_SR_class(self) -> None:
        pass

    @final
    def process(self, img: np.ndarray) -> np.ndarray:
        """
        set target size, and process image
        :param img: img to process
        :return:
        """
        if self._targetscale <= 0:  # upscale once, return directly
            img = self._process_n(img)

        else:  # upscale multiple times
            self._target_size = (math.ceil(img.shape[1] * self._targetscale),
                                 math.ceil(img.shape[0] * self._targetscale))
            img = self._process_n(img)
            img = self._process_downscale(img)

        return img

    @final
    def _process_downscale(self, img: np.ndarray) -> np.ndarray:
        if abs(self._targetscale - float(self._modelscale ** self._sr_n)) < 1e-3:
            return img
        # use bicubic interpolation for image downscaling
        img = cv2.resize(img, self._target_size, interpolation=cv2.INTER_CUBIC)
        return img

    @final
    def _process_n(self, img: np.ndarray) -> np.ndarray:
        for _ in range(self._sr_n):
            img = self._SR_class.process_cv2(img)
        return img
