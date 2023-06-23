import pytest

from src.SRqueue import SR_queue
from test.util import load_image, getSRCONFIG, calculate_image_similarity


class Test_SRQUEUE:
    def test_case_srqueue(self):
        config = getSRCONFIG()
        config.targetscale = 1.14514
        SR_queue()
