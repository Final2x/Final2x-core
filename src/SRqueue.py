import cv2
import numpy as np
from pathlib import Path
from loguru import logger

from src.SRFactory import SRFactory
from src.utils.getConfig import SRCONFIG


def SR_queue():
    config = SRCONFIG()
    input_path: list = config.inputpath
    output_path: Path = Path(config.outputpath) / "outputs"
    output_path.mkdir(parents=True, exist_ok=True)  # create output folder
    sr = SRFactory.getSR()
    for img_path in input_path:
        save_path = str(output_path /
                        (Path(
                            str(config.targetscale) + 'x-' + Path(img_path).name).stem + '.png'
                         ))

        i: int = 0
        while Path(save_path).is_file():
            i += 1
            save_path = str(output_path /
                            (Path(
                                str(config.targetscale) + 'x-' + Path(img_path).name).stem + '(' + str(i) + ').png'
                             ))

        if Path(img_path).is_file():
            logger.info("Processing: " + img_path + ", save to: " + save_path)
            img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
            img = sr.process(img)
            cv2.imencode('.png', img)[1].tofile(save_path)
        else:
            logger.warning("File not found: " + img_path + ", skip. Save path: " + save_path)
