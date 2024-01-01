import os
from pathlib import Path


def GithubAction_PIP_Test():
    projectPATH = Path(__file__).resolve().parent.parent.absolute()
    p_yaml = str(projectPATH / "config.yaml")
    os.system("Final2x-core -y " + p_yaml)


if __name__ == "__main__":
    GithubAction_PIP_Test()
