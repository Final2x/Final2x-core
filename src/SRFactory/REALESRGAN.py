from loguru import logger

try:
    from src.SRFactory.SRBaseClass import SRBaseClass
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory.SRBaseClass import SRBaseClass


class REALESRGAN(SRBaseClass):
    def __init__(self):
        super().__init__()

        self._init_SR_class()

    @logger.catch(reraise=True)
    def _init_SR_class(self) -> None:

        try:
            from src.SRncnn.REALESRGANncnn import REALESRGANncnn
        except ImportError:
            # for pip cli
            from Final2x_core.src.SRncnn.REALESRGANncnn import Realesrgan as REALESRGANncnn

        # model_dict = {
        #     0: {"param": "realesr-animevideov3-x2.param", "bin": "realesr-animevideov3-x2.bin", "scale": 2},
        #     1: {"param": "realesr-animevideov3-x3.param", "bin": "realesr-animevideov3-x3.bin", "scale": 3},
        #     2: {"param": "realesr-animevideov3-x4.param", "bin": "realesr-animevideov3-x4.bin", "scale": 4},
        #     3: {"param": "realesrgan-x4plus-anime.param", "bin": "realesrgan-x4plus-anime.bin", "scale": 4},
        #     4: {"param": "realesrgan-x4plus.param", "bin": "realesrgan-x4plus.bin", "scale": 4}
        # }
        model_i = 0
        if self._model == "RealESRGAN-animevideov3":
            if self._modelscale == 2:
                model_i = 0
            elif self._modelscale == 3:
                model_i = 1
            elif self._modelscale == 4:
                model_i = 2
            else:
                logger.warning("RealESRGAN-animevideov3 only support scale 2, 3, 4. Auto set to 2")
                model_i = 0  # default to it
                self._reset_modelscale(2)

        elif self._model == "RealESRGAN-anime":
            if self._modelscale == 4:
                model_i = 3
            else:
                logger.warning("RealESRGAN-anime only support scale 4. Auto set to 4")
                model_i = 3
                self._reset_modelscale(4)

        elif self._model == "RealESRGAN":
            if self._modelscale == 4:
                model_i = 4
            else:
                logger.warning("RealESRGAN only support scale 4. Auto set to 4")
                model_i = 4
                self._reset_modelscale(4)

        else:
            logger.error("RealESRGAN model not implemented")
            raise NotImplementedError("RealESRGAN model not implemented")

        self._SR_class = REALESRGANncnn(gpuid=self._gpuid, model=model_i, tta_mode=self._tta)
        logger.info("RealESRGAN model loaded")
