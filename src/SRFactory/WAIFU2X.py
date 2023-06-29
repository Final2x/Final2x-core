from loguru import logger

try:
    from src.SRFactory.SRBaseClass import SRBaseClass
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory.SRBaseClass import SRBaseClass


class WAIFU2X(SRBaseClass):
    def __init__(self):
        super().__init__()

        self._init_SR_class()

    @logger.catch(reraise=True)
    def _init_SR_class(self) -> None:

        try:
            from src.SRncnn.WAIFU2Xncnn import WAIFU2Xncnn
        except ImportError:
            # for pip cli
            from Final2x_core.src.SRncnn.WAIFU2Xncnn import Waifu2x as WAIFU2Xncnn

        # waifu2x model name, can be "models-cunet",
        # "models-upconv_7_anime_style_art_rgb" and
        # "models-upconv_7_photo", default: models-cunet

        model_i = "models-cunet"
        if self._model == "Waifu2x-cunet":
            model_i = "models-cunet"

            if self._modelscale not in [1, 2]:
                logger.warning("Waifu2x-cunet modelscale should be in [1, 2]. Auto set to 2")
                self._reset_modelscale(2)

            if self._modelnoise not in [-1, 0, 1, 2, 3]:
                logger.warning("Waifu2x-cunet modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to 0")
                self._modelnoise = 0
            elif self._modelnoise == -1:
                if self._modelscale == 1:
                    logger.warning("Waifu2x-cunet modelnoise is -1, modelscale should be 2. Auto set to 2")
                    self._reset_modelscale(2)

        elif self._model == "Waifu2x-upconv_7_anime_style_art_rgb":
            model_i = "models-upconv_7_anime_style_art_rgb"

            if self._modelscale != 2:
                logger.warning("Waifu2x-upconv_7_anime_style_art_rgb modelscale should be 2. Auto set to 2")
                self._reset_modelscale(2)

            if self._modelnoise not in [-1, 0, 1, 2, 3]:
                logger.warning(
                    "Waifu2x-upconv_7_anime_style_art_rgb modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to 0")
                self._modelnoise = 0

        elif self._model == "Waifu2x-upconv_7_photo":
            model_i = "models-upconv_7_photo"

            if self._modelscale != 2:
                logger.warning("Waifu2x-upconv_7_photo modelscale should be 2. Auto set to 2")
                self._reset_modelscale(2)

            if self._modelnoise not in [-1, 0, 1, 2, 3]:
                logger.warning("Waifu2x-upconv_7_photo modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to 0")
                self._modelnoise = 0

        else:
            logger.error("Waifu2x model not implemented")
            raise NotImplementedError("Waifu2x model not implemented")

        self._SR_class = WAIFU2Xncnn(gpuid=self._gpuid, model=model_i, noise=self._modelnoise,
                                     scale=self._modelscale, tta_mode=self._tta)
        logger.info("Waifu2x model initialized")
