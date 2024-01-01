import sys

import pytest

from tests.util import calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_REALESRGAN:
    def test_case_RealESRGAN_animevideov3(self):
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN-animevideov3"
        for i in range(0, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealESRGAN_anime(self):
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN-anime"
        for i in range(3, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealESRGAN(self):
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN"
        for i in range(3, 6):
            config.modelscale = i
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self):
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            _ = REALESRGAN()
