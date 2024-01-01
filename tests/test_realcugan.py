import pytest

from tests.util import calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


class Test_REALCUGAN:
    def test_case_RealCUGAN_pro(self) -> None:
        from Final2x_core.src.SRFactory import REALCUGAN

        config = getSRCONFIG()
        config.model = "RealCUGAN-pro"  # type: ignore
        # test invalid scale and noise
        for s in range(1, 5):
            for n in range(-2, 5):
                config.modelscale = s  # type: ignore
                config.modelnoise = n  # type: ignore
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_RealCUGAN_se(self) -> None:
        from Final2x_core.src.SRFactory import REALCUGAN

        config = getSRCONFIG()
        config.model = "RealCUGAN-se"  # type: ignore
        for s in range(1, 6):
            for n in range(-2, 5):
                config.modelscale = s  # type: ignore
                config.modelnoise = n  # type: ignore
                SR = REALCUGAN()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self) -> None:
        from Final2x_core.src.SRFactory import REALCUGAN

        config = getSRCONFIG()
        config.model = "sb"  # type: ignore
        with pytest.raises(NotImplementedError):
            REALCUGAN()
