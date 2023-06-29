from loguru import logger

try:
    from src.SRFactory.SRBaseClass import SRBaseClass
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory.SRBaseClass import SRBaseClass


class SRMD(SRBaseClass):
    def __init__(self):
        super().__init__()

        self._init_SR_class()

    @logger.catch(reraise=True)
    def _init_SR_class(self) -> None:

        try:
            from src.SRncnn.SRMDncnn import SRMDncnn
        except ImportError:
            # for pip cli
            from Final2x_core.src.SRncnn.SRMDncnn import SRMD as SRMDncnn

        if self._modelnoise not in range(-1, 11):
            logger.warning("SRMD modelnoise must be in [-1, 10]. Auto set to 3")
            self._modelnoise = 3

        model_i = "models-srmd"
        if self._model == "SRMD":
            model_i = "models-srmd"

            if self._modelscale not in [2, 3, 4]:
                logger.warning("SRMD modelscale must in [2, 3, 4]. Auto set to 2")
                self._reset_modelscale(2)

        else:
            logger.error("SRMD model not implemented")
            raise NotImplementedError("SRMD model not implemented")

        self._SR_class = SRMDncnn(gpuid=self._gpuid, model=model_i, noise=self._modelnoise,
                                  scale=self._modelscale, tta_mode=self._tta)
        logger.info("SRMD model initialized")
