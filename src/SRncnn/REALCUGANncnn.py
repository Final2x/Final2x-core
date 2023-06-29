import pathlib

from realcugan_ncnn_py import Realcugan

try:
    from src.utils.getConfig import SRCONFIG
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.getConfig import SRCONFIG


class REALCUGANncnn(Realcugan):
    def _load(self, param_path: pathlib.Path = None, model_path: pathlib.Path = None) -> None:
        """
        Load models from root models folder.

        :param param_path: the path to model params. usually ended with ".param"
        :param model_path: the path to model bin. usually ended with ".bin"
        :return: None
        """
        if param_path is None or model_path is None:
            config = SRCONFIG()
            model_path = pathlib.Path(config.modelpath) / "RealCUGAN" / self._model

            if self._noise == -1:
                param_path = (
                        model_path
                        / f"up{self._scale}x-conservative.param"
                )
                model_path = (
                        model_path
                        / f"up{self._scale}x-conservative.bin"
                )
            elif self._noise == 0:
                param_path = (
                        model_path
                        / f"up{self._scale}x-no-denoise.param"
                )
                model_path = (
                        model_path / f"up{self._scale}x-no-denoise.bin"
                )
            else:
                param_path = (
                        model_path
                        / f"up{self._scale}x-denoise{self._noise}x.param"
                )
                model_path = (
                        model_path
                        / f"up{self._scale}x-denoise{self._noise}x.bin"
                )

        self._realcugan_object.load(str(param_path), str(model_path))
