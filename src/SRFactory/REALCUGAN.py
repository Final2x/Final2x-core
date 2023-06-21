import numpy as np

from src.SRFactory.SRBaseClass import SRBaseClass
from src.utils.getConfig import SRCONFIG


class REALCUGAN(SRBaseClass):
    def __init__(self):
        super().__init__()
        self.config = SRCONFIG()

        self._set_model()
        self._init_SR_class()

    def _set_model(self) -> str:
        return "REALCUGAN"

    def _init_SR_class(self) -> None:
        from src.SRncnn.REALCUGANncnn import REALCUGANncnn
        if self.config.model == "RealCUGAN-se":
            model_i = "models-se"
        elif self.config.model == "RealCUGAN-pro":
            model_i = "models-pro"
        else:
            raise NotImplementedError("model not implemented")
        self._SR_class = REALCUGANncnn(gpuid=self._gpuid, model=model_i)
