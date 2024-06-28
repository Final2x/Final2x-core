from typing import Any

from Final2x_core.src.utils.getConfig import SRCONFIG
from loguru import logger


class SRFactory:
    @staticmethod
    @logger.catch(reraise=True)
    def getSR() -> Any:
        """
        get a SR model instance according to config
        :return:
        """
        config = SRCONFIG()
        model = config.model

        if model in ["RealCUGAN-se", "RealCUGAN-pro"]:
            from . import REALCUGAN

            return REALCUGAN()

        elif model in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime", "APISR-RRDB"]:
            from . import REALESRGAN

            return REALESRGAN()

        elif model in ["Waifu2x-cunet", "Waifu2x-upconv_7_anime_style_art_rgb", "Waifu2x-upconv_7_photo"]:
            from . import WAIFU2X

            return WAIFU2X()

        else:
            logger.error("model not implemented")
            raise NotImplementedError("model not implemented")
