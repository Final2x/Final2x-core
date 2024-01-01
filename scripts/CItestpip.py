import os
from pathlib import Path

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def GithubAction_PIP_Test() -> None:
    p_yaml = str(projectPATH / "src/Final2x_core/config.yaml")
    os.system("Final2x-core -y " + p_yaml)


if __name__ == "__main__":
    GithubAction_PIP_Test()
