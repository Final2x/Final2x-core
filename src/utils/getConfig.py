import json
import base64
from pathlib import Path
from typing import Union

import yaml
from loguru import logger

try:
    from src.utils.singleton import singleton
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.singleton import singleton


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

    @logger.catch(reraise=True)
    def getConfigfromYaml(self, configpath: str = "", modelpath: str = "") -> None:
        """
        get config from yaml file
        :param configpath: absolute path to config file
        :param modelpath: absolute path to model folder
        :return:
        """
        self._modelpath: str = modelpath
        with open(configpath, 'r', encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self._setConfig(config)

    @logger.catch(reraise=True)
    def getConfigfromJson(self, config: str = "", modelpath: str = "") -> None:
        """
        get config from json string
        :param config: a json string
        :param modelpath: absolute path to model folder
        :return:
        """
        self._modelpath = modelpath
        config = json.loads(config)
        self._setConfig(config)

    @logger.catch(reraise=True)
    def getConfigfromBase64toJson(self, config: str = "", modelpath: str = "") -> None:
        """
        get config from base64 string
        :param config: a base64 string
        :param modelpath: absolute path to model folder
        :return:
        """
        self._modelpath = modelpath

        config = config.encode('utf-8')
        config = base64.b64decode(config).decode("utf-8")
        config = json.loads(config)
        self._setConfig(config)

    @logger.catch(reraise=True)
    def _setConfig(self, config: dict) -> None:
        self.outputpath = config["outputpath"]
        self.gpuid = config["gpuid"]
        self.tta = config["tta"]
        self.model = config["model"]
        self.modelscale = config["modelscale"]
        self.modelnoise = config["modelnoise"]
        self.inputpath = config["inputpath"]
        # targetscale should be set after modelscale
        self.targetscale = config["targetscale"]

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
    def inputpath(self) -> list:
        return self._inputpath

    @outputpath.setter
    def outputpath(self, value: str) -> None:
        if type(value) is not str:
            logger.error("outputpath must be str")
            raise TypeError("outputpath must be str")
        if not Path(value).is_dir():
            logger.error("outputpath must be a dir")
            raise TypeError("outputpath must be a dir")

        self._outputpath = value

    @targetscale.setter
    def targetscale(self, value: Union[int, float]) -> None:
        if type(value) is not int and type(value) is not float:
            logger.error("targetscale must be int or float")
            raise TypeError("targetscale must be int or float")
        if type(value) is not float:
            value = float(value)
        if value <= 0:
            self._targetscale = self._modelscale
        else:
            self._targetscale = value

    @gpuid.setter
    def gpuid(self, value: int) -> None:
        if type(value) is not int:
            logger.error("gpuid must be int")
            raise TypeError("gpuid must be int")
        self._gpuid = value

    @tta.setter
    def tta(self, value: bool) -> None:
        if type(value) is not bool:
            logger.error("tta must be bool")
            raise TypeError("tta must be bool")
        self._tta = value

    @model.setter
    def model(self, value: str) -> None:
        if type(value) is not str:
            logger.error("model must be str")
            raise TypeError("model must be str")
        self._model = value

    @modelscale.setter
    def modelscale(self, value: int) -> None:
        if type(value) is not int:
            logger.error("modelscale must be int")
            raise TypeError("modelscale must be int")
        self._modelscale = value

    @modelnoise.setter
    def modelnoise(self, value: int) -> None:
        if type(value) is not int:
            logger.error("modelnoise must be int")
            raise TypeError("modelnoise must be int")
        self._modelnoise = value

    @inputpath.setter
    def inputpath(self, value: list) -> None:
        if type(value) is not list:
            logger.error("inputpath must be list")
            raise TypeError("inputpath must be list")
        if len(value) == 0:
            logger.error("inputpath must not be empty")
            raise ValueError("inputpath must not be empty")
        self._inputpath = value
