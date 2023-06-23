import cv2
import yaml
from pathlib import Path

if __name__ == '__main__':
    projectPATH = Path(__file__).resolve().parent.parent.absolute()

    gpuid: int = 0  # -1 for CPU, > 0 for GPU
    # use cpu if gpu is not available
    if not cv2.ocl.haveOpenCL():
        gpuid = -1

    print(f"gpuid: {gpuid}")

    p_dict = {
        "gpuid"      : gpuid,
        "inputpath"  : [
            "./1/1/4/5/1/4/1/9/1/9/8/1/0.jpg",
            str(projectPATH / "assets" / "herta.jpg"),
            str(projectPATH / "assets" / "herta.jpg"),
            str(projectPATH / "assets" / "final2x-10.png"),
            str(projectPATH / "assets" / "final2x-20.png"),
            str(projectPATH / "assets" / "final2x-40.png"),
            str(projectPATH / "assets" / "final2x-80.png"),
            str(projectPATH / "assets" / "final2x-160.png"),
            str(projectPATH / "assets" / "final2x-320.png"),
            str(projectPATH / "assets" / "final2x-640.png"),
            str(projectPATH / "assets" / "final2x-1280.png"),
        ],
        "model"      : "RealCUGAN-pro",
        "modelscale" : 2,
        "modelnoise" : 1,
        "outputpath" : str(projectPATH / "assets"),
        "targetscale": 2,
        "tta"        : True,
    }

    p_model: str = str(projectPATH / "models")
    p_yaml = str(projectPATH / "config.yaml")

    print(f"p_model: {p_model}")
    print(f"p_yaml: {p_yaml}")

    with open(p_yaml, 'w', encoding='utf-8') as f:
        yaml.safe_dump(p_dict, f)
