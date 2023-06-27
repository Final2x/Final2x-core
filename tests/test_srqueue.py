import pytest

from src.SRqueue import SR_queue
from tests.util import load_image, getSRCONFIG, calculate_image_similarity


class Test_SRQUEUE:
    def test_case_srqueue(self):
        config = getSRCONFIG()
        config.targetscale = 1.14514
        SR_queue()

    def test_case_srqueue_negative(self):
        config = getSRCONFIG()
        config._targetscale = -1.14514  # force negative
        SR_queue()

    def test_case_srqueue_zero(self):
        config = getSRCONFIG()
        config._targetscale = 0  # force zero
        SR_queue()
