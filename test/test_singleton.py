from src.utils.getConfig import SRCONFIG


class Test_singleton:
    def test_config_class(self):
        c1 = SRCONFIG()
        c2 = SRCONFIG()
        c3 = SRCONFIG()
        assert c1 == c2 == c3
