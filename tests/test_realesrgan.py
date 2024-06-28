import sys

import pytest

from tests.util import calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_REALESRGAN:
    def test_case_RealESRGAN_animevideov3(self) -> None:
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN-animevideov3"  # type: ignore
        for i in range(0, 6):
            config.modelscale = i  # type: ignore
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealESRGAN_anime(self) -> None:
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN-anime"  # type: ignore
        for i in range(3, 6):
            config.modelscale = i  # type: ignore
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealESRGAN(self) -> None:
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "RealESRGAN"  # type: ignore
        for i in range(3, 6):
            config.modelscale = i  # type: ignore
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_APISR_RRDB(self) -> None:
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "APISR-RRDB"  # type: ignore
        for i in range(3, 6):
            config.modelscale = i  # type: ignore
            SR = REALESRGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self) -> None:
        from Final2x_core.src.SRFactory import REALESRGAN

        config = getSRCONFIG()
        config.model = "sb"  # type: ignore
        with pytest.raises(NotImplementedError):
            REALESRGAN()
