import pytest

from tests.util import load_image, getSRCONFIG, calculate_image_similarity


class Test_REALCUGAN:
    def test_case_RealCUGAN_pro(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-pro"
        # test invalid scale and noise
        for s in range(1, 4):
            for n in range(-2, 4):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)

    def test_case_RealCUGAN_se(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-se"
        for s in range(1, 5):
            for n in range(-1, 5):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)

    def test_case_invalid_model(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            SR = REALCUGAN()
            img1 = load_image()
            _ = SR.process(img1)
