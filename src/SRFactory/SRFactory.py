from src.SRFactory import REALCUGAN
from src.SRFactory import REALESRGAN

from src.utils.getConfig import SRCONFIG


class SRFactory:
    @staticmethod
    def getSR():
        config = SRCONFIG()
        model = config.model
        if model in ["RealCUGAN-se", "RealCUGAN-pro"]:
            return REALCUGAN()
        elif model in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            if config.gpuid == -1:
                raise Exception("GPU is required for RealESRGAN")
            return REALESRGAN()
        else:
            raise NotImplementedError("model not implemented")
