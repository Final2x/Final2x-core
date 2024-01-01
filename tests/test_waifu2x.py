import sys

import pytest

from tests.util import calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_WAIFU2X:
    def test_case_Waifu2x_cunet(self) -> None:
        from Final2x_core.src.SRFactory import WAIFU2X

        config = getSRCONFIG()
        config.model = "Waifu2x-cunet"  # type: ignore
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s  # type: ignore
                config.modelnoise = i  # type: ignore
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_Waifu2x_upconv_7_anime_style_art_rgb(self) -> None:
        from Final2x_core.src.SRFactory import WAIFU2X

        config = getSRCONFIG()
        config.model = "Waifu2x-upconv_7_anime_style_art_rgb"  # type: ignore
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s  # type: ignore
                config.modelnoise = i  # type: ignore
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_Waifu2x_upconv_7_photo(self) -> None:
        from Final2x_core.src.SRFactory import WAIFU2X

        config = getSRCONFIG()
        config.model = "Waifu2x-upconv_7_photo"  # type: ignore
        for s in range(0, 4):
            for i in range(-2, 5):
                config.modelscale = s  # type: ignore
                config.modelnoise = i  # type: ignore
                SR = WAIFU2X()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self) -> None:
        from Final2x_core.src.SRFactory import WAIFU2X

        config = getSRCONFIG()
        config.model = "sb"  # type: ignore
        with pytest.raises(NotImplementedError):
            WAIFU2X()
