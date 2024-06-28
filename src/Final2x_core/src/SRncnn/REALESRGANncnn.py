import pathlib
from typing import Dict, Optional, Union

from Final2x_core.src.utils.getConfig import SRCONFIG
from realesrgan_ncnn_py import Realesrgan


class REALESRGANncnn(Realesrgan):  # type: ignore
    def _load(
        self, param_path: Optional[pathlib.Path] = None, model_path: Optional[pathlib.Path] = None, scale: int = 0
    ) -> None:
        """
        Load models from root models folder.

        :param param_path: the path to model params. usually ended with ".param"
        :param model_path: the path to model bin. usually ended with ".bin"
        :param scale: the scale of the model. 1, 2, 3, 4...
        :return: None
        """
        config = SRCONFIG()
        # if self._model == -1:
        #     if param_path is None and model_path is None and scale == 0:
        #         raise ValueError("param_path, model_path and scale must be specified when model == -1")
        #     if param_path is None or model_path is None:
        #         raise ValueError("param_path and model_path must be specified when model == -1")
        #     if scale == 0:
        #         raise ValueError("scale must be specified when model == -1")
        # else:
        _path = pathlib.Path(config.modelpath) / "RealESRGAN"

        model_dict: Dict[int, Dict[str, Union[str, int]]] = {
            0: {"param": "realesr-animevideov3-x2.param", "bin": "realesr-animevideov3-x2.bin", "scale": 2},
            1: {"param": "realesr-animevideov3-x3.param", "bin": "realesr-animevideov3-x3.bin", "scale": 3},
            2: {"param": "realesr-animevideov3-x4.param", "bin": "realesr-animevideov3-x4.bin", "scale": 4},
            3: {"param": "realesrgan-x4plus-anime.param", "bin": "realesrgan-x4plus-anime.bin", "scale": 4},
            4: {"param": "realesrgan-x4plus.param", "bin": "realesrgan-x4plus.bin", "scale": 4},
            5: {"param": "APISR-RRDB-x4.param", "bin": "APISR-RRDB-x4.bin", "scale": 4},
        }

        param_path = _path / model_dict[self._model]["param"]  # type: ignore
        model_path = _path / model_dict[self._model]["bin"]  # type: ignore

        self._scale = scale if scale == -1 else model_dict[self._model]["scale"]
        self._set_parameters()

        self._realesrgan_object.load(str(param_path), str(model_path))
