from loguru import logger

try:
    from src.SRFactory.SRBaseClass import SRBaseClass
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory.SRBaseClass import SRBaseClass


class REALCUGAN(SRBaseClass):
    def __init__(self):
        super().__init__()

        self._init_SR_class()

    @logger.catch(reraise=True)
    def _init_SR_class(self) -> None:

        try:
            from src.SRncnn.REALCUGANncnn import REALCUGANncnn
        except ImportError:
            # for pip cli
            from Final2x_core.src.SRncnn.REALCUGANncnn import Realcugan as REALCUGANncnn

        if self._model == "RealCUGAN-se":
            model_i = "models-se"

            if self._modelscale == 2:
                if self._modelnoise not in [-1, 0, 1, 2, 3]:
                    logger.warning("RealCUGAN-se modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to -1")
                    self._modelnoise = -1
            elif self._modelscale == 3:
                if self._modelnoise not in [-1, 0, 3]:
                    logger.warning("RealCUGAN-se modelnoise should be in [-1, 0, 3]. Auto set to -1")
                    self._modelnoise = -1
            elif self._modelscale == 4:
                if self._modelnoise not in [-1, 0, 3]:
                    logger.warning("RealCUGAN-se modelnoise should be in [-1, 0, 3]. Auto set to -1")
                    self._modelnoise = -1
            else:
                logger.warning("RealCUGAN-se modelscale should be in [2, 3, 4]. Auto set to 2")
                self._reset_modelscale(2)
                logger.warning("RealCUGAN-se modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to -1")
                self._modelnoise = -1

        elif self._model == "RealCUGAN-pro":
            model_i = "models-pro"

            if self._modelscale not in [2, 3]:
                logger.warning("RealCUGAN-pro modelscale should be in [2, 3]. Auto set to 2")
                self._reset_modelscale(2)

            if self._modelnoise not in [-1, 0, 3]:
                logger.warning("RealCUGAN-pro modelnoise should be in [-1, 0, 3]. Auto set to -1")
                self._modelnoise = -1

        else:
            logger.error("RealCUGAN model not implemented")
            raise NotImplementedError("RealCUGAN model not implemented")

        self._SR_class = REALCUGANncnn(gpuid=self._gpuid, model=model_i, noise=self._modelnoise,
                                       scale=self._modelscale, tta_mode=self._tta, )
        logger.info("RealCUGAN model initialized")
