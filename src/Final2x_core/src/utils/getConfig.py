import base64
import json
from pathlib import Path
from typing import Dict, List, Optional, Union

import yaml
from Final2x_core.src.utils.singleton import singleton
from loguru import logger


@singleton
class SRCONFIG:
    def __init__(self) -> None:
        self._modelpath: str = ""
        self._outputpath: str = ""
        self._targetscale: float = 2.0
        self._gpuid: int = 0
        self._tta: bool = False
        self._model: str = "RealCUGAN-pro"
        self._modelscale: int = 2
        self._modelnoise: int = 0
        self._inputpath: List[str] = []
        self.isfrozen: bool = False

    @logger.catch(reraise=True)
    def getConfigfromYaml(self, configpath: str = "", modelpath: str = "") -> None:
        """
        get config from yaml file
        :param configpath: absolute path to config file
        :param modelpath: absolute path to model folder
        :return:
        """
        self._modelpath = modelpath
        with open(configpath, "r", encoding="utf-8") as f:
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
        self._setConfig(json.loads(config))

    @logger.catch(reraise=True)
    def getConfigfromBase64toJson(self, config: str = "", modelpath: str = "") -> None:
        """
        get config from base64 string
        :param config: a base64 string
        :param modelpath: absolute path to model folder
        :return:
        """
        self._modelpath = modelpath

        config_bytes = config.encode("utf-8")
        config_json_str = base64.b64decode(config_bytes).decode("utf-8")
        config_dict = json.loads(config_json_str)
        self._setConfig(config_dict)

    @logger.catch(reraise=True)
    def _setConfig(self, config: Optional[Dict[str, Union[str, int, float, bool, List[str]]]]) -> None:
        self.outputpath = config["outputpath"]  # type: ignore
        self.gpuid = config["gpuid"]  # type: ignore
        self.tta = config["tta"]  # type: ignore
        self.model = config["model"]  # type: ignore
        self.modelscale = config["modelscale"]  # type: ignore
        self.modelnoise = config["modelnoise"]  # type: ignore
        self.inputpath = config["inputpath"]  # type: ignore
        # targetscale should be set after modelscale
        self.targetscale = config["targetscale"]  # type: ignore

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

    @outputpath.setter  # type: ignore
    def outputpath(self, value: str) -> None:
        if type(value) is not str:
            logger.error("outputpath must be str")
            raise TypeError("outputpath must be str")
        if not Path(value).is_dir():
            logger.error("outputpath must be a dir")
            raise TypeError("outputpath must be a dir")

        self._outputpath = value

    @targetscale.setter  # type: ignore
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

    @gpuid.setter  # type: ignore
    def gpuid(self, value: int) -> None:
        if type(value) is not int:
            logger.error("gpuid must be int")
            raise TypeError("gpuid must be int")
        self._gpuid = value

    @tta.setter  # type: ignore
    def tta(self, value: bool) -> None:
        if type(value) is not bool:
            logger.error("tta must be bool")
            raise TypeError("tta must be bool")
        self._tta = value

    @model.setter  # type: ignore
    def model(self, value: str) -> None:
        if type(value) is not str:
            logger.error("model must be str")
            raise TypeError("model must be str")
        self._model = value

    @modelscale.setter  # type: ignore
    def modelscale(self, value: int) -> None:
        if type(value) is not int:
            logger.error("modelscale must be int")
            raise TypeError("modelscale must be int")
        self._modelscale = value

    @modelnoise.setter  # type: ignore
    def modelnoise(self, value: int) -> None:
        if type(value) is not int:
            logger.error("modelnoise must be int")
            raise TypeError("modelnoise must be int")
        self._modelnoise = value

    @inputpath.setter  # type: ignore
    def inputpath(self, value: list) -> None:
        if type(value) is not list:
            logger.error("inputpath must be list")
            raise TypeError("inputpath must be list")
        if len(value) == 0:
            logger.error("inputpath must not be empty")
            raise ValueError("inputpath must not be empty")
        self._inputpath = value
