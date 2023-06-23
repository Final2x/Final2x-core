import sys
import pytest

from tests.util import load_image, CONFIG, getSRCONFIG, calculate_image_similarity


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_REALESRGAN:
    @pytest.mark.skipif(CONFIG()[0] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN_animevideov3(self):
        from src.SRFactory import REALESRGAN
        config = getSRCONFIG()
        config.model = "RealESRGAN-animevideov3"
        for i in range(0, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[0] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN_anime(self):
        from src.SRFactory import REALESRGAN
        config = getSRCONFIG()
        config.model = "RealESRGAN-anime"
        for i in range(3, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[0] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN(self):
        from src.SRFactory import REALESRGAN
        config = getSRCONFIG()
        config.model = "RealESRGAN"
        for i in range(3, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)

    def test_case_invalid_model(self):
        from src.SRFactory import REALESRGAN
        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            SR = REALESRGAN()
