import sys
import pytest

from tests.util import load_image, CONFIG, getSRCONFIG, calculate_image_similarity, compare_image_size


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_WAIFU2X:
    @pytest.mark.skipif(sys.platform == "linux" and CONFIG()[0] == -1, reason="Skipping test when running on Linux CPU")
    def test_case_Waifu2x_cunet(self):
        from src.SRFactory import WAIFU2X
        config = getSRCONFIG()
        config.model = "Waifu2x-cunet"
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s
                config.modelnoise = i
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_Waifu2x_upconv_7_anime_style_art_rgb(self):
        from src.SRFactory import WAIFU2X
        config = getSRCONFIG()
        config.model = "Waifu2x-upconv_7_anime_style_art_rgb"
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s
                config.modelnoise = i
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_Waifu2x_upconv_7_photo(self):
        from src.SRFactory import WAIFU2X
        config = getSRCONFIG()
        config.model = "Waifu2x-upconv_7_photo"
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s
                config.modelnoise = i
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self):
        from src.SRFactory import WAIFU2X
        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            SR = WAIFU2X()
