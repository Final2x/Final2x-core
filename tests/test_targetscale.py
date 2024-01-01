from tests.util import calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


class Test_TARGETSCALE:
    def test_case_targetscale_positive(self) -> None:
        from Final2x_core.src.SRFactory import REALCUGAN

        config = getSRCONFIG()
        config.model = "RealCUGAN-pro"  # type: ignore
        for t in [7.99999, 1, 2, 2.5, 4, 5.6619, 8, 10]:
            config.targetscale = t  # type: ignore
            SR = REALCUGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, config.targetscale)

    def test_case_targetscale_negative(self) -> None:
        from Final2x_core.src.SRFactory import REALCUGAN

        config = getSRCONFIG()
        config.model = "RealCUGAN-se"  # type: ignore
        for t in [0, 0.00, -114, -514.114, -1919810]:
            config.targetscale = t  # type: ignore
            SR = REALCUGAN()
            img1 = load_image()
            img2 = SR.process(img1)
            assert calculate_image_similarity(img1, img2)
            assert (
                img2.shape[0] == img1.shape[0] * config.modelscale
                and img2.shape[1] == img1.shape[1] * config.modelscale
            )
