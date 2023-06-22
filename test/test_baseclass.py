import pytest


class Test_SRBaseClass:
    def test_init_error(self):
        from src.SRFactory.SRBaseClass import SRBaseClass
        with pytest.raises(TypeError):
            _ = SRBaseClass()
