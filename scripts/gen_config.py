import os
from pathlib import Path

import yaml

projectPATH = Path(__file__).resolve().parent.parent.absolute()

_GPUID_ = 0
# gpuid = -1 when in GitHub Actions
if os.environ.get("GITHUB_ACTIONS") == "true":
    _GPUID_ = -1

print("-" * 50)


def gen_config() -> None:
    gpuid = _GPUID_

    if gpuid == -1:
        print("GitHub Actions detected. Using CPU.")
    else:
        print(f"Not in GitHub Actions. Using GPU {gpuid}.")

    p_dict = {
        "gpuid": gpuid,
        "inputpath": [
            "./1/1/4/5/1/4/1/9/1/9/8/1/0.jpg",
            str(projectPATH / "assets" / "gray.jpg"),
            str(projectPATH / "assets" / "herta.jpg"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-20.png"),
            str(projectPATH / "assets" / "final2x-40.png"),
            str(projectPATH / "assets" / "final2x-80.png"),
            str(projectPATH / "assets" / "final2x-160.png"),
            str(projectPATH / "assets" / "final2x-320.png"),
            str(projectPATH / "assets" / "herta-unix-pic.exe"),
            str(projectPATH / "assets" / "vulkan-1.dll"),
        ],
        "model": "RealCUGAN-pro",
        "modelscale": 2,
        "modelnoise": 1,
        "outputpath": str(projectPATH / "assets"),
        "targetscale": 2,
        "tta": False,
    }

    p_yaml = str(projectPATH / "src/Final2x_core/config.yaml")

    with open(p_yaml, "w", encoding="utf-8") as f:
        yaml.safe_dump(p_dict, f)

    print("Config generated at " + p_yaml)


if __name__ == "__main__":
    gen_config()
