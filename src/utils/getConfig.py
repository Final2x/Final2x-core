import yaml

from src.utils.singleton import singleton


@singleton
class SRCONFIG:
    def __init__(self):
        self.modelpath: str = ""
        self.outputpath: str = ""
        self.targetscale: float = 2.0
        self.gpuid: int = 0
        self.tta: bool = False
        self.model: str = "RealCUGAN-pro"
        self.modelscale: int = 2
        self.modelnoise: int = 0
        self.alphavalue: float = 1.0
        self.inputpath: list[str] = []

    def getConfig(self, configpath: str = "", modelpath: str = "") -> None:
        self.modelpath: str = modelpath
        with open(configpath, 'r', encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self.outputpath: str = config["outputpath"]
        self.targetscale: float = config["targetscale"]
        self.gpuid: int = config["gpuid"]
        self.tta: bool = config["tta"]
        self.model: str = config["model"]
        self.modelscale: int = config["modelscale"]
        self.modelnoise: int = config["modelnoise"]
        self.alphavalue: float = config["alphavalue"]
        self.inputpath: list[str] = config["inputpath"]
