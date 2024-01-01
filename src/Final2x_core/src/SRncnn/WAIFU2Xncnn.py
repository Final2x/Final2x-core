import pathlib
from typing import Optional

from Final2x_core.src.utils.getConfig import SRCONFIG
from waifu2x_ncnn_py import Waifu2x


class WAIFU2Xncnn(Waifu2x):  # type: ignore
    def _load(self, param_path: Optional[pathlib.Path] = None, model_path: Optional[pathlib.Path] = None) -> None:
        """
        Load models from root models folder.

        :param param_path: the path to model params. usually ended with ".param"
        :param model_path: the path to model bin. usually ended with ".bin"
        :return: None
        """
        if param_path is None or model_path is None:
            config = SRCONFIG()
            _path = pathlib.Path(config.modelpath) / "Waifu2x" / self._model

            if self._noise == -1:
                param_path = _path / "scale2.0x_model.param"
                model_path = _path / "scale2.0x_model.bin"
                self._scale = 2
            elif self._scale == 1:
                param_path = _path / f"noise{self._noise}_model.param"
                model_path = _path / f"noise{self._noise}_model.bin"
            elif self._scale == 2:
                param_path = _path / f"noise{self._noise}_scale2.0x_model.param"
                model_path = _path / f"noise{self._noise}_scale2.0x_model.bin"

        self._waifu2x_object.load(str(param_path), str(model_path))
