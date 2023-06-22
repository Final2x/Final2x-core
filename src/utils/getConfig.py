import yaml
import json
from typing import Union

from src.utils.singleton import singleton


@singleton
class SRCONFIG:
    def __init__(self):
        self._modelpath: str = ""
        self._outputpath: str = ""
        self._targetscale: float = 2.0
        self._gpuid: int = 0
        self._tta: bool = False
        self._model: str = "RealCUGAN-pro"
        self._modelscale: int = 2
        self._modelnoise: int = 0
        self._inputpath: list = []

    def getConfigfromYaml(self, configpath: str = "", modelpath: str = "") -> None:
        self._modelpath: str = modelpath
        with open(configpath, 'r', encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self._setConfig(config)

    def getConfigfromJson(self, config: str = "", modelpath: str = "") -> None:
        """
        get config from json string
        :param config: a json string
        :param modelpath: path to model folder
        :return:
        """
        self._modelpath: str = modelpath
        config = json.loads(config)
        self._setConfig(config)

    def _setConfig(self, config: dict) -> None:
        self.outputpath = config["outputpath"]
        self.targetscale = config["targetscale"]
        self.gpuid = config["gpuid"]
        self.tta = config["tta"]
        self.model = config["model"]
        self.modelscale = config["modelscale"]
        self.modelnoise = config["modelnoise"]
        self.inputpath = config["inputpath"]

    @property
    def modelpath(self) -> str:
        return self._modelpath

    @property
    def outputpath(self) -> str:
        return self._outputpath

    @property
    def targetscale(self) -> float:
        return self._targetscale

    @property
    def gpuid(self) -> int:
        return self._gpuid

    @property
    def tta(self) -> bool:
        return self._tta

    @property
    def model(self) -> str:
        return self._model

    @property
    def modelscale(self) -> int:
        return self._modelscale

    @property
    def modelnoise(self) -> int:
        return self._modelnoise

    @property
    def inputpath(self) -> list[str]:
        return self._inputpath

    @outputpath.setter
    def outputpath(self, value: str) -> None:
        if type(value) is not str:
            raise TypeError("outputpath must be str")
        self._outputpath = value

    @targetscale.setter
    def targetscale(self, value: Union[int, float]) -> None:
        if type(value) is not int and type(value) is not float:
            raise TypeError("targetscale must be int or float")
        if type(value) is not float:
            value = float(value)
        self._targetscale = value

    @gpuid.setter
    def gpuid(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("gpuid must be int")
        self._gpuid = value

    @tta.setter
    def tta(self, value: bool) -> None:
        if type(value) is not bool:
            raise TypeError("tta must be bool")
        self._tta = value

    @model.setter
    def model(self, value: str) -> None:
        if type(value) is not str:
            raise TypeError("model must be str")
        self._model = value

    @modelscale.setter
    def modelscale(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("modelscale must be int")
        self._modelscale = value

    @modelnoise.setter
    def modelnoise(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("modelnoise must be int")
        self._modelnoise = value

    @inputpath.setter
    def inputpath(self, value: list) -> None:
        if type(value) is not list:
            raise TypeError("inputpath must be list")
        self._inputpath = value
