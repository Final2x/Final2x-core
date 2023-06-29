try:
    from src.SRFactory.SRFactory import SRFactory
    from src.SRFactory.REALCUGAN import REALCUGAN
    from src.SRFactory.REALESRGAN import REALESRGAN
    from src.SRFactory.WAIFU2X import WAIFU2X
    from src.SRFactory.SRMD import SRMD
except ImportError:
    # for pip cli
    from Final2x_core.src.SRFactory.SRFactory import SRFactory
    from Final2x_core.src.SRFactory.REALCUGAN import REALCUGAN
    from Final2x_core.src.SRFactory.REALESRGAN import REALESRGAN
    from Final2x_core.src.SRFactory.WAIFU2X import WAIFU2X
    from Final2x_core.src.SRFactory.SRMD import SRMD

__all__ = [SRFactory, REALCUGAN, REALESRGAN, WAIFU2X, SRMD]
