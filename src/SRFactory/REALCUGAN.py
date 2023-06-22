from src.SRFactory.SRBaseClass import SRBaseClass


class REALCUGAN(SRBaseClass):
    def __init__(self):
        super().__init__()

        self._init_SR_class()

    def _init_SR_class(self) -> None:
        from src.SRncnn.REALCUGANncnn import REALCUGANncnn

        if self._model == "RealCUGAN-se":
            model_i = "models-se"

            if self._modelscale not in [2, 3, 4]:
                print("RealCUGAN-se modelscale should be in [2, 3, 4]. Auto set to 2")
                self._modelscale = 2

            if self._modelscale == 2:
                if self._modelnoise not in [-1, 0, 1, 2, 3]:
                    print("RealCUGAN-se modelnoise should be in [-1, 0, 1, 2, 3]. Auto set to -1")
                    self._modelnoise = -1
            elif self._modelscale == 3:
                if self._modelnoise not in [-1, 0, 3]:
                    print("RealCUGAN-se modelnoise should be in [-1, 0, 3]. Auto set to -1")
                    self._modelnoise = -1
            elif self._modelscale == 4:
                if self._modelnoise not in [-1, 0, 3]:
                    print("RealCUGAN-se modelnoise should be in [-1, 0, 3]. Auto set to -1")
                    self._modelnoise = -1

        elif self._model == "RealCUGAN-pro":
            model_i = "models-pro"

            if self._modelscale not in [2, 3]:
                print("RealCUGAN-pro modelscale should be in [2, 3]. Auto set to 2")
                self._modelscale = 2

            if self._modelnoise not in [-1, 0, 3]:
                print("RealCUGAN-pro modelnoise should be in [-1, 0, 3]. Auto set to -1")
                self._modelnoise = -1
        else:
            raise NotImplementedError("model not implemented")

        self._SR_class = REALCUGANncnn(gpuid=self._gpuid, model=model_i, noise=self._modelnoise,
                                       scale=self._modelscale)
