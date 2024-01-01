import sys

import pytest
from Final2x_core import SRFactory

from tests.util import getSRCONFIG


class Test_GETSR:
    def test_case_invalid_model(self) -> None:
        config = getSRCONFIG()
        config.model = "1145141919810"  # type: ignore
        with pytest.raises(NotImplementedError):
            _ = SRFactory.getSR()

    def test_case_REALCUGAN(self) -> None:
        config = getSRCONFIG()
        for m in ["RealCUGAN-se", "RealCUGAN-pro"]:
            config.model = m  # type: ignore
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALCUGAN"

    @pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test due to use CPU or macOS")
    def test_case_REALESRGAN(self) -> None:
        config = getSRCONFIG()
        for m in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            config.model = m  # type: ignore
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "REALESRGAN"

    @pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
    def test_case_WAIFU2X(self) -> None:
        config = getSRCONFIG()
        for m in ["Waifu2x-cunet", "Waifu2x-upconv_7_anime_style_art_rgb", "Waifu2x-upconv_7_photo"]:
            config.model = m  # type: ignore
            SR = SRFactory.getSR()
            assert type(SR).__name__ == "WAIFU2X"
