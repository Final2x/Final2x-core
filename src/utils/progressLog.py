from loguru import logger

try:
    from src.utils.singleton import singleton
except ImportError:
    # for pip cli
    from Final2x_core.src.utils.singleton import singleton


@singleton
class PrintProgressLog:
    def __init__(self):
        """
        Total: Total Process Time
        """

        self.Total = 0
        self.progressCurrent = 0
        self.sr_n = 1

    @logger.catch(reraise=True)
    def set(self, total_file: int, sr_n: int) -> None:
        if total_file <= 0:
            raise AssertionError("Total must be greater than 0")
        if sr_n < 1:
            raise AssertionError("sr_n must be greater than 1")
        self.Total = total_file * sr_n
        self.sr_n = sr_n

    @logger.catch
    def printProgress(self) -> None:
        self.progressCurrent += 1
        percentage: float = round(self.progressCurrent / self.Total * 100, 1)
        logger.info("Processing------[ " + str(percentage) + "% ]")

    @logger.catch
    def skipProgress(self) -> None:
        for _ in range(self.sr_n):
            self.printProgress()
