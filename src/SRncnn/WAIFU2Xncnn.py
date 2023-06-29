import pathlib

from waifu2x_ncnn_py import Waifu2x

try:
    from src.utils.getConfig import SRCONFIG
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.getConfig import SRCONFIG


class WAIFU2Xncnn(Waifu2x):
    def _load(
            self, param_path: pathlib.Path = None, model_path: pathlib.Path = None
    ) -> None:
        """
        Load models from root models folder.

        :param param_path: the path to model params. usually ended with ".param"
        :param model_path: the path to model bin. usually ended with ".bin"
        :return: None
        """
        if param_path is None or model_path is None:
            config = SRCONFIG()
            model_path = pathlib.Path(config.modelpath) / "Waifu2x" / self._model

            if self._noise == -1:
                param_path = model_path / "scale2.0x_model.param"
                model_path = model_path / "scale2.0x_model.bin"
                self._scale = 2
            elif self._scale == 1:
                param_path = model_path / f"noise{self._noise}_model.param"
                model_path = model_path / f"noise{self._noise}_model.bin"
            elif self._scale == 2:
                param_path = model_path / f"noise{self._noise}_scale2.0x_model.param"
                model_path = model_path / f"noise{self._noise}_scale2.0x_model.bin"

        self._waifu2x_object.load(str(param_path), str(model_path))
