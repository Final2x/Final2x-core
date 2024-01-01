# download models from https://github.com/Tohrusky/model-zoo
import os
import shutil
import zipfile
from pathlib import Path
from typing import Dict

import requests
import tqdm

model_dict: Dict[str, str] = {
    "RealCUGAN": "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/RealCUGAN.zip",
    "RealESRGAN": "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/RealESRGAN.zip",
    "Waifu2x": "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/Waifu2x.zip",
}

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def download_model(model_name: str) -> None:
    if model_name not in model_dict:
        raise ValueError(f"Unknown model name: {model_name}")

    model_path = projectPATH / f"src/Final2x_core/models/{model_name}"
    if os.path.exists(model_path):
        return

    url = model_dict[model_name]
    r = requests.get(url, stream=True)

    with open(f"{model_name}.zip", "wb") as f:
        shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile(f"{model_name}.zip", "r") as zip_ref:
        zip_ref.extractall(f"{model_name}")

    # copy model to Final2x_core/models
    shutil.copytree(f"{model_name}/{model_name}", model_path)

    os.remove(f"{model_name}.zip")
    shutil.rmtree(f"{model_name}")


def download_all() -> None:
    print("-" * 50)
    print("Downloading models...")
    print("-" * 50)
    for model_name in tqdm.tqdm(model_dict.keys()):
        download_model(model_name)


if __name__ == "__main__":
    download_all()
