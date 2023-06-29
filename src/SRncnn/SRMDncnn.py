import pathlib

from srmd_ncnn_py import SRMD

try:
    from src.utils.getConfig import SRCONFIG
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.getConfig import SRCONFIG


class SRMDncnn(SRMD):
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
            model_path = pathlib.Path(config.modelpath) / "SRMD" / self._model

            if self._noise == -1:
                param_path = model_path / f"srmdnf_x{self._scale}.param"
                model_path = model_path / f"srmdnf_x{self._scale}.bin"
            else:
                param_path = model_path / f"srmd_x{self._scale}.param"
                model_path = model_path / f"srmd_x{self._scale}.bin"

        self._srmd_object.load(str(param_path), str(model_path))
