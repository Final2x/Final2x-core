import argparse
import os
import sys
from pathlib import Path

from loguru import logger

from Final2x_core.download_models import download_all
from Final2x_core.src.SRqueue import SR_queue
from Final2x_core.src.utils.getConfig import SRCONFIG

_IS_FROZEN_ = False

if getattr(sys, "frozen", False):
    # frozen
    _IS_FROZEN_ = True
    projectPATH = Path(sys.executable).parent.absolute()
else:
    # unfrozen
    projectPATH = Path(__file__).resolve().parent.absolute()

# parse args
parser = argparse.ArgumentParser()
parser.description = "when para is not specified, the config.yaml file in the directory will be read automatically"
parser.add_argument("-b", "--BASE64", help="base64 string for config json", type=str)
parser.add_argument("-j", "--JSON", help="JSON string for config", type=str)
parser.add_argument("-y", "--YAML", help="yaml config file path", type=str)
parser.add_argument("-l", "--LOG", help="save log", action="store_true")
parser.add_argument("-c", "--CACHE", help="cache models", action="store_true")
parser.add_argument("-n", "--NOTOPENFOLDER", help="don't open output folder", action="store_true")
args = parser.parse_args()

if args.CACHE:
    download_all()
    exit(0)


def open_folder(path: str) -> None:
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform.startswith("darwin"):
            os.system('open "{}"'.format(path))
        elif sys.platform.startswith("linux"):
            os.system('xdg-open "{}"'.format(path))
        else:
            logger.error("cannot open output folder")
    except Exception as e:
        logger.error(e)
        logger.error("cannot open output folder")


def main() -> None:
    entries = os.listdir(projectPATH / "models")
    if len(entries) <= 1:  # first time run
        download_all()

    if args.LOG:
        # init logger
        logger.add(projectPATH / "logs" / "log-{time}.log", encoding="utf-8", retention="60 days")
    logger.info("projectPATH: " + str(projectPATH))

    # load config
    config = SRCONFIG()
    if args.BASE64 is not None:
        config.getConfigfromBase64toJson(str(args.BASE64), str(projectPATH / "models"))
    elif args.JSON is not None:
        config.getConfigfromJson(str(args.JSON), str(projectPATH / "models"))
    elif args.YAML is not None:
        config.getConfigfromYaml(str(args.YAML), str(projectPATH / "models"))
    else:
        config.getConfigfromYaml(str(projectPATH / "config.yaml"), str(projectPATH / "models"))

    config.isfrozen = _IS_FROZEN_

    logger.info("config loaded")
    logger.debug(config.outputpath)

    SR_queue()

    logger.success("______SR_COMPLETED______")

    if not args.NOTOPENFOLDER:
        OP = Path(config.outputpath) / "outputs"
        open_folder(str(OP))


if __name__ == "__main__":
    main()
