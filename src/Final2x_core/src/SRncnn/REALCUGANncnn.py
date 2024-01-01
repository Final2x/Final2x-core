import pathlib
from typing import Optional

from Final2x_core.src.utils.getConfig import SRCONFIG
from realcugan_ncnn_py import Realcugan


class REALCUGANncnn(Realcugan):  # type: ignore
    def _load(self, param_path: Optional[pathlib.Path] = None, model_path: Optional[pathlib.Path] = None) -> None:
        """
        Load models from root models folder.

        :param param_path: the path to model params. usually ended with ".param"
        :param model_path: the path to model bin. usually ended with ".bin"
        :return: None
        """
        if param_path is None or model_path is None:
            config = SRCONFIG()
            _path = pathlib.Path(config.modelpath) / "RealCUGAN" / self._model

            if self._noise == -1:
                param_path = _path / f"up{self._scale}x-conservative.param"
                model_path = _path / f"up{self._scale}x-conservative.bin"
            elif self._noise == 0:
                param_path = _path / f"up{self._scale}x-no-denoise.param"
                model_path = _path / f"up{self._scale}x-no-denoise.bin"
            else:
                param_path = _path / f"up{self._scale}x-denoise{self._noise}x.param"
                model_path = _path / f"up{self._scale}x-denoise{self._noise}x.bin"

        self._realcugan_object.load(str(param_path), str(model_path))
