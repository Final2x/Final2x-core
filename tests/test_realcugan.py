import pytest

from tests.util import load_image, getSRCONFIG, calculate_image_similarity, compare_image_size


class Test_REALCUGAN:
    def test_case_RealCUGAN_pro(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-pro"
        # test invalid scale and noise
        for s in range(1, 5):
            for n in range(-2, 5):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealCUGAN_se(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-se"
        for s in range(1, 6):
            for n in range(-2, 5):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            SR = REALCUGAN()
