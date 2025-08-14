import json

from box import ConfigBox
from dataEngineer import logger   
from ensure import ensure_annotations
import os
from pathlib import Path

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)

        if verbose:
            logger.info(f"created directory at : {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"Json file loaded succesfully from: {path}")
    return ConfigBox(content)