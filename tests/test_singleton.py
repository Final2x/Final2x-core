from Final2x_core.src.utils.getConfig import SRCONFIG
from Final2x_core.src.utils.progressLog import PrintProgressLog
from Final2x_core.src.utils.singleton import singleton


class Test_SINGLETON:
    def test_srconfig(self) -> None:
        c1 = SRCONFIG()
        c2 = SRCONFIG()
        c3 = SRCONFIG()
        assert c1 == c2 == c3

    def test_progresslog(self) -> None:
        p1 = PrintProgressLog()
        p2 = PrintProgressLog()
        p3 = PrintProgressLog()
        assert p1 == p2 == p3

    def test_singleton_instance(self) -> None:
        class MyClass:
            def __init__(self, value: int):
                self.value = value

        instance1 = MyClass(1145141919810)
        instance2 = singleton(instance1)  # type: ignore

        assert instance1 == instance2
        assert instance1.value == instance2.value
