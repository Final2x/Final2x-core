import math

from test.util import load_image, getSRCONFIG, calculate_image_similarity


class Test_TARGETSCALE:
    def test_case_targetscale_positive(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-pro"
        for t in [7.99999, 1, 2, 2.5, 4, 5.6619, 8, 10]:
            config.targetscale = t
            SR = REALCUGAN()
            img1 = load_image()
            target_size = (math.ceil(img1.shape[1] * t),
                           math.ceil(img1.shape[0] * t))
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert img2.shape[0] == target_size[0] and img2.shape[1] == target_size[1]

    def test_case_targetscale_negative(self):
        from src.SRFactory import REALCUGAN
        config = getSRCONFIG()
        config.model = "RealCUGAN-se"
        for t in [0, 0.00, -114, -514.114, -1919810]:
            config.targetscale = t
            SR = REALCUGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert img2.shape[0] == img1.shape[0] * config.modelscale and \
                   img2.shape[1] == img1.shape[1] * config.modelscale
