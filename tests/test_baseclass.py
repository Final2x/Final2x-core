import pytest


class Test_SRBASECLASS:
    def test_init_error(self) -> None:
        from Final2x_core.src.SRFactory.SRBaseClass import SRBaseClass

        with pytest.raises(TypeError):
            SRBaseClass()  # type: ignore
