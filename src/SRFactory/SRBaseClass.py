from abc import ABC, abstractmethod
import numpy as np
import cv2
from typing import final

from src.utils.getConfig import SRCONFIG


class SRBaseClass(ABC):
    def __init__(self):
        config = SRCONFIG()
        self._target_scale = config.targetscale  # user upscale factor
        self._tta = config.tta  # use tta
        self._gpuid = config.gpuid  # gpu id, -1 for cpu

        self._model_scale = 2  # model upscale factor, override in child class
        self._sr_n = 1  # upscale n times, override in child class
        self._SR_class = None  # upscale model, override in child class

        self._target_size: tuple[int, int] = (0, 0)  # target size of the image

        print("SRBaseClass init")

    @abstractmethod
    def _set_model(self) -> str:
        pass

    @abstractmethod
    def _init_SR_class(self) -> None:
        pass

    @final
    def process(self, img: np.ndarray) -> np.ndarray:
        self._target_size = (int(img.shape[1] * self._target_scale), int(img.shape[0] * self._target_scale))
        img = self._process_n(img)
        img = self._process_downscale(img)
        return img

    @final
    def _process_downscale(self, img: np.ndarray) -> np.ndarray:
        if self._target_scale == self._model_scale ** self._sr_n:
            return img
        # use bicubic interpolation for image downscaling
        img = cv2.resize(img, self._target_size, interpolation=cv2.INTER_CUBIC)
        return img

    @final
    def _process_n(self, img: np.ndarray) -> np.ndarray:
        for _ in range(self._sr_n):
            img = self._SR_class.process_cv2(img)
        return img
