import shutil
import sys
from pathlib import Path

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def post_pyinstaller() -> None:
    print("-" * 50)
    shutil.copytree(projectPATH / "src/Final2x_core/models", projectPATH / "dist/Final2x-core/models")
    shutil.copy(projectPATH / "src/Final2x_core/config.yaml", projectPATH / "dist/Final2x-core/config.yaml")
    print("Copied models and config to dist folder~")

    if sys.platform == "win32":
        shutil.copy(projectPATH / "assets/vulkan-1.dll", projectPATH / "dist/Final2x-core/vulkan-1.dll")
        print("Copied vulkan-1.dll to dist folder~")

    print("-" * 50)


if __name__ == "__main__":
    post_pyinstaller()
