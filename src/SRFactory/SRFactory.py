from loguru import logger


class SRFactory:
    @staticmethod
    @logger.catch(reraise=True)
    def getSR():
        from src.utils.getConfig import SRCONFIG
        config = SRCONFIG()
        model = config.model

        if model in ["RealCUGAN-se", "RealCUGAN-pro"]:
            from src.SRFactory import REALCUGAN
            return REALCUGAN()

        elif model in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            if config.gpuid == -1:
                logger.error("GPU is required for RealESRGAN")
                raise Exception("GPU is required for RealESRGAN")
            from src.SRFactory import REALESRGAN
            return REALESRGAN()

        elif model in ["Waifu2x-cunet", "Waifu2x-upconv_7_anime_style_art_rgb", "Waifu2x-upconv_7_photo"]:
            from src.SRFactory import WAIFU2X
            return WAIFU2X()

        else:
            logger.error("model not implemented")
            raise NotImplementedError("model not implemented")
