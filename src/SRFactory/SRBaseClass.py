import math
from abc import ABC, abstractmethod
from typing import final

import cv2
import numpy as np
from loguru import logger

try:
    from src.utils.getConfig import SRCONFIG
    from src.utils.progressLog import PrintProgressLog
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.getConfig import SRCONFIG
    from Final2x_core.src.utils.progressLog import PrintProgressLog


class SRBaseClass(ABC):
    def __init__(self):
        config = SRCONFIG()
        self._targetscale: float = config.targetscale  # user upscale factor
        self._gpuid: int = config.gpuid  # gpu id, -1 for cpu
        self._tta: bool = config.tta  # use tta
        self._model: str = config.model  # model name
        self._modelscale: int = config.modelscale  # model upscale factor
        self._modelnoise: int = config.modelnoise  # model noise level

        self._sr_n = 1  # super-resolution times
        self._set_sr_n()

        self._SR_class = None  # upscale model, override in child class

        self._target_size: tuple[int, int] = (0, 0)  # target size of the image

        logger.info("SRBaseClass init")

    @final
    @logger.catch
    def _set_sr_n(self) -> None:
        """
        set super-resolution times, when targetscale > modelscale
        :return:
        """
        config = SRCONFIG()

        if self._modelscale <= 1:  # 1x model, or wrong model scale, call _reset_modelscale to set it
            PrintProgressLog().set(len(config.inputpath), 1)
            return
        s: int = self._modelscale
        while self._targetscale > s:
            self._sr_n += 1
            s *= self._modelscale
        logger.info("sr_n set to " + str(self._sr_n))

        PrintProgressLog().set(len(config.inputpath), self._sr_n)

    @abstractmethod
    def _init_SR_class(self) -> None:
        """
        init SR_class, override in child class
        :return:
        """

    @final
    @logger.catch
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
    @logger.catch
    def _process_downscale(self, img: np.ndarray) -> np.ndarray:
        if abs(self._targetscale - float(self._modelscale ** self._sr_n)) < 1e-3:
            return img
        # use bicubic interpolation for image downscaling
        img = cv2.resize(img, self._target_size, interpolation=cv2.INTER_CUBIC)
        return img

    @final
    @logger.catch
    def _process_n(self, img: np.ndarray) -> np.ndarray:
        for _ in range(self._sr_n):
            img = self._SR_class.process_cv2(img)
            PrintProgressLog().printProgress()
        return img

    @final
    @logger.catch
    def _reset_modelscale(self, modelscale: int) -> None:
        """
        reset modelscale, and call _set_sr_n
        :param modelscale: reseted scale factor of the model
        :return:
        """
        self._modelscale = modelscale
        logger.info("modelscale reset to " + str(self._modelscale))
        self._set_sr_n()
