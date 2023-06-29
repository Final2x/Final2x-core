import argparse
import os
import sys
from pathlib import Path

import cv2
from loguru import logger

try:
    from src.SRqueue import SR_queue
    from src.utils.getConfig import SRCONFIG
except ImportError:
    # for pip cli
    from Final2x_core.src.SRqueue import SR_queue
    from Final2x_core.src.utils.getConfig import SRCONFIG

# python -m pytest --cov=src --cov-report=html
# python -m PyInstaller -n Final2x-core -i assets/favicon.ico __main__.py
if getattr(sys, 'frozen', False):
    # frozen
    projectPATH = Path(sys.executable).parent.absolute()
else:
    # unfrozen
    projectPATH = Path(__file__).resolve().parent.absolute()

logger.add(projectPATH / "logs" / "log-{time}.log", encoding="utf-8", retention="60 days")

logger.info("projectPATH: " + str(projectPATH))

parser = argparse.ArgumentParser()
parser.description = "when -j is not specified, the config.yaml file in the directory will be read automatically"
parser.add_argument("-j", "--JSON", help="JSON str for config", type=str)
args = parser.parse_args()

config = SRCONFIG()
if args.JSON is None:
    config.getConfigfromYaml(str(projectPATH / "config.yaml"), str(projectPATH / "models"))
else:
    config.getConfigfromJson(str(args.JSON), str(projectPATH / "models"))

logger.info("config loaded")
# use cpu if gpu is not available
if not cv2.ocl.haveOpenCL() and config.gpuid != -1:
    logger.warning("gpu is not available, use cpu instead")
    config.gpuid = -1

SR_queue()

logger.success("______SR_COMPLETED______")


def open_folder(path: str) -> None:
    try:
        if sys.platform.startswith('win'):
            os.startfile(path)
        elif sys.platform.startswith('darwin'):
            os.system('open "{}"'.format(path))
        elif sys.platform.startswith('linux'):
            os.system('xdg-open "{}"'.format(path))
        else:
            logger.error("cannot open output folder")
    except Exception as e:
        logger.error(e)
        logger.error("cannot open output folder")


OP = Path(config.outputpath) / "outputs"
open_folder(str(OP))
