import sys
import pytest

from test.util import load_image, getSRCONFIG, CONFIG, calculate_image_similarity


class Test_GETSR:
    def test_case_invalid_model(self):
        from src.SRFactory import SRFactory
        config = getSRCONFIG()
        config.model = "1145141919810"
        with pytest.raises(NotImplementedError):
            _ = SRFactory.getSR()

    def test_case_REALCUGAN(self):
        from src.SRFactory import SRFactory
        config = getSRCONFIG()
        for m in ["RealCUGAN-se", "RealCUGAN-pro"]:
            config.model = m
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALCUGAN"

    @pytest.mark.skipif(CONFIG()[0] == -1 or sys.platform == "darwin", reason="Skipping test due to use CPU or macOS")
    def test_case_REALESRGAN(self):
        from src.SRFactory import SRFactory
        config = getSRCONFIG()
        for m in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            config.model = m
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALESRGAN"

    def test_case_get_REALESRGAN_error(self):
        from src.SRFactory import SRFactory
        config = getSRCONFIG()
        config.model = "RealESRGAN-animevideov3"
        config.gpuid = -1
        with pytest.raises(Exception):
            _ = SRFactory.getSR()
