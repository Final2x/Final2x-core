import numpy as np

from src.SRFactory.SRBaseClass import SRBaseClass
from src.utils.getConfig import SRCONFIG


class REALESRGAN(SRBaseClass):
    def __init__(self):
        super().__init__()
        self.config = SRCONFIG()

        self._set_model()
        self._init_SR_class()

    def _set_model(self) -> str:
        return "REALESRGAN"

    def _init_SR_class(self) -> None:
        from src.SRncnn.REALESRGANncnn import REALESRGANncnn
        model_i = 0
        # ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]
        if self.config.model == "RealESRGAN-animevideov3":
            pass
        self._SR_class = REALESRGANncnn(gpuid=self._gpuid, model=model_i)
