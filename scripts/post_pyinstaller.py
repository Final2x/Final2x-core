import shutil
from pathlib import Path

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def copy_models_and_config() -> None:
    shutil.copytree(projectPATH / "src/Final2x_core/models", projectPATH / "dist/Final2x-core/models")
    shutil.copy(projectPATH / "src/Final2x_core/config.yaml", projectPATH / "dist/Final2x-core/config.yaml")

    print("-" * 50)
    print("Copied models and config to dist folder~")
    print("-" * 50)


if __name__ == "__main__":
    copy_models_and_config()
