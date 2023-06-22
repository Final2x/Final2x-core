import math

from test.util import load_image, CONFIG, calculate_image_similarity
from src.utils.getConfig import SRCONFIG


class Test_TARGETSCALE:
    def test_case_targetscale_positive(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealCUGAN-pro"
        for t in [1, 2, 2.5, 4, 5.6619, 8, 10]:
            config.targetscale = t
            SR = REALCUGAN()
            img1 = load_image()
            target_size = (math.ceil(img1.shape[1] * t),
                           math.ceil(img1.shape[0] * t))
            img2 = SR.process(img1)
            print("img1.shape: ", img1.shape)
            print("img2.shape: ", img2.shape)
            assert calculate_image_similarity(img1, img2)
            assert img2.shape[0] == target_size[0] and img2.shape[1] == target_size[1]

    def test_case_targetscale_negative(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealCUGAN-se"
        for t in [0, 0.00, -114, -514.114, -1919810]:
            config.targetscale = t
            SR = REALCUGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            print("img1.shape: ", img1.shape)
            print("img2.shape: ", img2.shape)
            assert calculate_image_similarity(img1, img2)
            assert img2.shape[0] == img1.shape[0] * config.modelscale and \
                   img2.shape[1] == img1.shape[1] * config.modelscale
