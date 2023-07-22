from loguru import logger


class SRFactory:
    @staticmethod
    @logger.catch(reraise=True)
    def getSR():
        """
        get a SR model instance according to config
        :return:
        """
        try:
            from src.utils.getConfig import SRCONFIG
        except ImportError:
            # for pip cli
            from Final2x_core.src.utils.getConfig import SRCONFIG

        config = SRCONFIG()
        model = config.model

        if model in ["RealCUGAN-se", "RealCUGAN-pro"]:

            try:
                from src.SRFactory import REALCUGAN
            except ImportError:
                # for pip cli
                from Final2x_core.src.SRFactory import REALCUGAN

            return REALCUGAN()

        elif model in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            if config.gpuid == -1:
                logger.error("GPU is required for RealESRGAN")
                raise Exception("GPU is required for RealESRGAN")

            try:
                from src.SRFactory import REALESRGAN
            except ImportError:
                # for pip cli
                from Final2x_core.src.SRFactory import REALESRGAN

            return REALESRGAN()

        elif model in ["Waifu2x-cunet", "Waifu2x-upconv_7_anime_style_art_rgb", "Waifu2x-upconv_7_photo"]:

            try:
                from src.SRFactory import WAIFU2X
            except ImportError:
                # for pip cli
                from Final2x_core.src.SRFactory import WAIFU2X

            return WAIFU2X()

        elif model in ["SRMD"]:
            if config.gpuid == -1:
                logger.error("GPU is required for SRMD")
                raise Exception("GPU is required for SRMD")

            try:
                from src.SRFactory import SRMD
            except ImportError:
                # for pip cli
                from Final2x_core.src.SRFactory import SRMD

            return SRMD()

        else:
            logger.error("model not implemented")
            raise NotImplementedError("model not implemented")
