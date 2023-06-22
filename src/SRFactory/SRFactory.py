class SRFactory:
    @staticmethod
    def getSR():
        from src.utils.getConfig import SRCONFIG
        config = SRCONFIG()
        model = config.model
        if model in ["RealCUGAN-se", "RealCUGAN-pro"]:
            from src.SRFactory import REALCUGAN
            return REALCUGAN()
        elif model in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            if config.gpuid == -1:
                raise Exception("GPU is required for RealESRGAN")
            from src.SRFactory import REALESRGAN
            return REALESRGAN()
        else:
            raise NotImplementedError("model not implemented")
