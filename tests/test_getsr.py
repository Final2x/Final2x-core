import sys

import pytest
from Final2x_core.src.SRFactory import SRFactory

from tests.util import CONFIG, getSRCONFIG


class Test_GETSR:
    def test_case_invalid_model(self):
        config = getSRCONFIG()
        config.model = "1145141919810"
        with pytest.raises(NotImplementedError):
            _ = SRFactory.getSR()

    def test_case_REALCUGAN(self):
        config = getSRCONFIG()
        for m in ["RealCUGAN-se", "RealCUGAN-pro"]:
            config.model = m
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALCUGAN"

    @pytest.mark.skipif(CONFIG()[0] == -1 or sys.platform == "darwin", reason="Skipping test due to use CPU or macOS")
    def test_case_REALESRGAN(self):
        config = getSRCONFIG()
        for m in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            config.model = m
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALESRGAN"

    @pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
    def test_case_WAIFU2X(self):
        config = getSRCONFIG()
        for m in ["Waifu2x-cunet", "Waifu2x-upconv_7_anime_style_art_rgb", "Waifu2x-upconv_7_photo"]:
            config.model = m
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "WAIFU2X"
