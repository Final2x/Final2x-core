import base64

import pytest
from Final2x_core.src.utils.getConfig import SRCONFIG

from tests.util import CONFIG


class Test_SRCONFIG:
    def test_case_getConfigfromJson(self) -> None:
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[1], CONFIG()[3])

    def test_case_getConfigfromBase64toJson(self) -> None:
        config = SRCONFIG()
        b_bytes = base64.b64encode(CONFIG()[1].encode("utf-8"))
        b_str = b_bytes.decode("utf-8")
        config.getConfigfromBase64toJson(b_str, CONFIG()[3])

    def test_case_getConfigfromJson_Error(self) -> None:
        config = SRCONFIG()
        with pytest.raises(KeyError):
            config.getConfigfromJson(r'{"gpuid":0}', "sb114514")

    def test_case_getConfigfromYaml(self) -> None:
        config = SRCONFIG()
        config.getConfigfromYaml(CONFIG()[2], CONFIG()[3])

    def test_case_getConfigfromYaml_Error(self) -> None:
        config = SRCONFIG()
        with pytest.raises(FileNotFoundError):
            config.getConfigfromYaml("sb114514", "sb114514")

    def test_case_Settter_Error(self) -> None:
        config = SRCONFIG()
        with pytest.raises(TypeError):
            config.outputpath = 1  # type: ignore
        with pytest.raises(TypeError):
            config.outputpath = "/114514-1919810-114514"  # type: ignore
        with pytest.raises(TypeError):
            config.targetscale = 0  # type: ignore
            config.targetscale = -1  # type: ignore
            config.targetscale = -114.514  # type: ignore
            config.targetscale = 2  # type: ignore
            config.targetscale = "1"  # type: ignore
        with pytest.raises(TypeError):
            config.gpuid = "1"  # type: ignore
        with pytest.raises(TypeError):
            config.tta = 114514  # type: ignore
        with pytest.raises(TypeError):
            config.model = True  # type: ignore
        with pytest.raises(TypeError):
            config.modelscale = "1"  # type: ignore
        with pytest.raises(TypeError):
            config.modelnoise = "1"  # type: ignore
        with pytest.raises(TypeError):
            config.inputpath = False  # type: ignore
        with pytest.raises(ValueError):
            config.inputpath = []  # type: ignore
