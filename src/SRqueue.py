from pathlib import Path

import cv2
import numpy as np
from loguru import logger

try:
    from src.SRFactory import SRFactory
    from src.utils.getConfig import SRCONFIG
    from src.utils.progressLog import PrintProgressLog
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory import SRFactory
    from Final2x_core.src.utils.getConfig import SRCONFIG
    from Final2x_core.src.utils.progressLog import PrintProgressLog


def SR_queue():
    """
    Super-resolution queue. Process all RGBA images according to the config.
    :return:
    """
    config = SRCONFIG()
    input_path: list = config.inputpath
    output_path: Path = Path(config.outputpath) / "outputs"
    output_path.mkdir(parents=True, exist_ok=True)  # create output folder
    sr = SRFactory.getSR()

    logger.info("Processing------[ 0.0% ]")

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

        if not Path(img_path).is_file():
            logger.error("File not found: " + img_path + ", skip. Save path: " + save_path)
            logger.warning("______Skip_Image______: " + img_path)
            PrintProgressLog().skipProgress()

        else:
            alpha_channel = None

            try:
                # The file may not be read correctly.
                # In unix-like system, the Filename Extension is not important.
                img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                if img.shape[2] == 4:
                    logger.warning("4 channels image detected.")
                    PrintProgressLog().Total += PrintProgressLog().sr_n
                    # Extract alpha channel
                    alpha_channel = img[:, :, 3]
                    # Remove alpha channel from the image
                    img = img[:, :, :3]

                if img is None:
                    raise Exception('Failed to decode image.')
            except Exception as e:
                logger.error(str(e))
                logger.warning("CV2 load image failed: " + img_path + ", skip. ")
                logger.warning("______Skip_Image______: " + img_path)
                PrintProgressLog().skipProgress()
                continue

            logger.info("Processing: " + img_path + ", save to: " + save_path)
            img = sr.process(img)

            if alpha_channel is not None:
                # Stack alpha channel into a 3-channel tensor (AAA)
                alpha_tensor = np.dstack((alpha_channel, alpha_channel, alpha_channel))
                # Apply super-resolution to the alpha tensor
                alpha_tensor = sr.process(alpha_tensor)
                # Merge processed RGB channels with processed alpha tensor
                img = np.dstack((img, alpha_tensor[:, :, 0]))

            cv2.imencode('.png', img)[1].tofile(save_path)

            logger.success("______Process_Completed______: " + img_path)
