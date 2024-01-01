import sys

import pytest

from tests.util import CONFIG, calculate_image_similarity, compare_image_size, getSRCONFIG, load_image


@pytest.mark.skipif(sys.platform == "darwin", reason="Skipping test when running on macOS")
class Test_SRMD:
    @pytest.mark.skipif(CONFIG()[0] == -1, reason="Skipping test due to use CPU")
    def test_case_SRMD(self):
        from src.SRFactory import SRMD

        config = getSRCONFIG()
        config.model = "SRMD"
        for s in range(1, 6):
            for i in range(-2, 12):
                config.modelscale = s
                config.modelnoise = i
                SR = SRMD()
                img1 = load_image()
                img2 = SR.process(img1)
                assert calculate_image_similarity(img1, img2)
                assert compare_image_size(img1, img2, config.targetscale)

    def test_case_invalid_model(self):
        from src.SRFactory import SRMD

        config = getSRCONFIG()
        config.model = "sb"
        with pytest.raises(NotImplementedError):
            SR = SRMD()
