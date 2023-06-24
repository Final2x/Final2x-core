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
            logger.warning("Image already exists: " + save_path)
            i += 1
            save_path = str(output_path /
                            (Path(
                                str(config.targetscale) + 'x-' + Path(img_path).name).stem + '(' + str(i) + ').png'
                             ))
            logger.warning("Try to save to: " + save_path)

        if Path(img_path).is_file():
            try:
                # The file may not be read correctly.
                # In unix-like system, the Filename Extension is not important.
                img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
                if img is None:
                    raise Exception('Failed to decode image.')
            except Exception as e:
                logger.error(str(e))
                logger.warning("CV2 load image failed: " + img_path + ", skip. ")
                logger.warning("Skip Image: " + img_path)
                continue

            logger.info("Processing: " + img_path + ", save to: " + save_path)
            img = sr.process(img)
            cv2.imencode('.png', img)[1].tofile(save_path)

            logger.success("Process Completed: " + img_path)

        else:
            logger.error("File not found: " + img_path + ", skip. Save path: " + save_path)
            logger.warning("Skip Image: " + img_path)
