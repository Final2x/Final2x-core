from src.utils.getConfig import SRCONFIG
from src.utils.singleton import singleton


class Test_singleton:
    def test_config_class(self):
        c1 = SRCONFIG()
        c2 = SRCONFIG()
        c3 = SRCONFIG()
        assert c1 == c2 == c3

    def test_singleton_instance(self):
        class MyClass:
            def __init__(self, value: int):
                self.value = value

        instance1 = MyClass(1145141919810)
        instance2 = singleton(instance1)

        assert instance1 == instance2
        assert instance1.value == instance2.value
