# download models from https://github.com/Tohrusky/model-zoo
import hashlib
import os
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Dict, List

import requests
import tqdm

if getattr(sys, "frozen", False):
    # frozen
    projectPATH = Path(sys.executable).parent.absolute()
else:
    # unfrozen
    projectPATH = Path(__file__).resolve().parent.absolute()


# model name, url and hash
model_dict: Dict[str, List[str]] = {
    "RealCUGAN": [
        "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/RealCUGAN-240628.zip",
        "6f9d1f3fd06354647f33414c265b855b5bf5b41dacc80c00ce2fcdd56f9de8a6",
    ],
    "RealESRGAN": [
        "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/RealESRGAN-240628.zip",
        "7408c4c865847ffb3dd98aa9375edddcc7eadc584239752d3d9e32129a5cf719",
    ],
    "Waifu2x": [
        "https://github.com/Tohrusky/model-zoo/releases/download/v2.0.0/Waifu2x-240628.zip",
        "edae59c6f30a39d0d798a077d39eb2a62d156076d8f632c0854b2f0ae782d313",
    ],
}


def hash_directory(directory_path: Path) -> str:
    """
    Calculate the SHA-256 hash of all files in a directory.
    """

    def hash_file(filepath: Path) -> str:
        """
        Calculate the SHA-256 hash of a file.
        """
        hash_sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    files_list = []
    for root, _, files in os.walk(directory_path):
        for filename in files:
            filepath = Path(os.path.join(root, filename))
            files_list.append(hash_file(filepath))

    # Sort by file path to ensure consistency of the result
    files_list.sort()
    # Concatenate the paths and hashes of all files
    concatenated_str = "".join([f"{hash}" for hash in files_list])
    # Calculate the final hash value
    final_hash_sha256 = hashlib.sha256()
    final_hash_sha256.update(concatenated_str.encode("utf-8"))
    return final_hash_sha256.hexdigest()


def download_model(model_name: str) -> None:
    if model_name not in model_dict:
        raise ValueError(f"Unknown model name: {model_name}")

    model_path = projectPATH / f"models/{model_name}"
    if os.path.exists(model_path):
        if hash_directory(model_path) == model_dict[model_name][1]:
            return
        else:
            print(f"Model {model_name} exists but hash does not match, Re_downloading...")
            shutil.rmtree(model_path)

    print(f"\nDownloading {model_name}...")
    url = model_dict[model_name][0]
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
    print("Rechecking models hash...")
    recheck_all()


def recheck_all() -> None:
    for model_name in model_dict.keys():
        download_model(model_name)


if __name__ == "__main__":
    download_all()
