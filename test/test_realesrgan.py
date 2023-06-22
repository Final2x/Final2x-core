import sys
import pytest

from test.util import load_image, CONFIG, calculate_image_similarity
from src.utils.getConfig import SRCONFIG


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_REALESRGAN:
    @pytest.mark.skipif(CONFIG()[2] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN_animevideov3(self):
        from src.SRFactory import REALESRGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealESRGAN-animevideov3"
        for i in range(2, 5):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            print("img1.shape: ", img1.shape)
            print("img2.shape: ", img2.shape)
            assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[2] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN_anime(self):
        from src.SRFactory import REALESRGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealESRGAN-anime"
        for i in range(2, 5):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            print("img1.shape: ", img1.shape)
            print("img2.shape: ", img2.shape)
            assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[2] == -1, reason="Skipping test due to use CPU")
    def test_case_RealESRGAN(self):
        from src.SRFactory import REALESRGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealESRGAN"
        for i in range(2, 5):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            print("img1.shape: ", img1.shape)
            print("img2.shape: ", img2.shape)
            assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[2] == -1, reason="Skipping test due to use CPU")
    def test_case_get_SR(self):
        from src.SRFactory import SRFactory
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])

        for m in ["RealESRGAN-animevideov3", "RealESRGAN", "RealESRGAN-anime"]:
            for s in range(2, 5):
                config.model = m
                config.modelscale = s
                SR = SRFactory.getSR()
                img1 = load_image()
                img2 = SR.process(img1)
                print("img1.shape: ", img1.shape)
                print("img2.shape: ", img2.shape)
                assert calculate_image_similarity(img1, img2)

    @pytest.mark.skipif(CONFIG()[2] != -1, reason="Skipping test due to use GPU")
    def test_case_get_SR_error(self):
        from src.SRFactory import SRFactory
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealESRGAN-animevideov3"
        with pytest.raises(Exception):
            _ = SRFactory.getSR()
