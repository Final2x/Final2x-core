from test.util import load_image, CONFIG, calculate_image_similarity
from src.utils.getConfig import SRCONFIG


class Test_REALCUGAN:
    def test_case_RealCUGAN_pro(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealCUGAN-pro"
        for s in range(2, 4):
            for n in range(-1, 4):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                print("img1.shape: ", img1.shape)
                print("img2.shape: ", img2.shape)
                assert calculate_image_similarity(img1, img2)

    def test_case_RealCUGAN_se(self):
        from src.SRFactory import REALCUGAN
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])
        config.model = "RealCUGAN-se"
        for s in range(2, 5):
            for n in range(-1, 4):
                config.modelscale = s
                config.modelnoise = n
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                print("img1.shape: ", img1.shape)
                print("img2.shape: ", img2.shape)
                assert calculate_image_similarity(img1, img2)

    def test_case_get_SR(self):
        from src.SRFactory import SRFactory
        config = SRCONFIG()
        config.getConfigfromJson(CONFIG()[0], CONFIG()[1])

        for m in ["RealCUGAN-se", "RealCUGAN-pro"]:
            for s in range(2, 5):
                for n in range(-1, 4):
                    config.model = m
                    config.modelscale = s
                    config.modelnoise = n
                    SR = SRFactory.getSR()
                    img1 = load_image()
                    img2 = SR.process(img1)
                    print("img1.shape: ", img1.shape)
                    print("img2.shape: ", img2.shape)
                    assert calculate_image_similarity(img1, img2)
