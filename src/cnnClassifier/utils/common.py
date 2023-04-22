import os
from box.exception import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox 
from pathlib import Path
from typing import AnyStr

@ensure_annotation
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and argument
    Args:
        path_to_yaml(str): path like input
    Raises :
       Value error : if yaml file is empty
       e: empty file

    Returns:
       configBox: ConfigBox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotation
def create_directories(path_to_directories: list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

        
@ensure_annotation
def save_json(path: Path, data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)