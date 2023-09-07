"""
common utils 
"""
import os
from pathlib import Path
import json
from typing import Any
import base64
from box.exceptions import BoxValueError
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from cnnClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, "r", encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file: %s loaded successfully", path_to_yaml)
            config = ConfigBox(content)
            return config
    except BoxValueError as exc:
        raise ValueError('Empty yaml file') from exc
    except Exception as ex:
        raise ex

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True) -> None:
    """
    Creates directories

    Args:
        path_to_directories (list): list of directories to create
    """
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        logger.info("directory: %s created successfully", dir_path)
        if verbose:
            logger.info("directory: %s created successfully", dir_path)

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a json file

    Args:
        path (Path): path like input
        data (dict): data to save in json file
    """
    with open(path, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info("json file: %s saved successfully", path)

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file

    Args:
        path (Path): path like input to binary file

    Returns:
        Any: object stored in binary file
    """
    # with open(path, "rb") as bin_file:
    data = joblib.load(path)
    logger.info("binary file: %s loaded successfully", path)
    return data

@ensure_annotations
def get_size(path: Path) -> Any:
    """
    Gets size of a file in KB

    Args:
        path (Path): path like input to file

    Returns:
        Any: size of file
    """
    size = f"~ {round(os.path.getsize(path) / 1024, 2)} KB"
    logger.info("file: %s size: %s", path, size)
    return size
