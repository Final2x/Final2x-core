from Final2x_core.src.SRqueue import SR_queue

from tests.util import getSRCONFIG


class Test_SRQUEUE:
    def test_case_srqueue(self) -> None:
        config = getSRCONFIG()
        config.targetscale = 1.14514  # type: ignore
        SR_queue()

    def test_case_srqueue_negative(self) -> None:
        config = getSRCONFIG()
        # force negative
        config._targetscale = -1.14514
        SR_queue()

    def test_case_srqueue_zero(self) -> None:
        config = getSRCONFIG()
        # force zero
        config._targetscale = 0
        SR_queue()
