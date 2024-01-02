import os
from box import ConfigBox
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
import yaml
from pathlib import Path
from typing import Any
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: str) ->ConfigBox :
    """
    reads yaml file and returns it in ConfigBox format

    Args:
        path_to_yaml: path to yaml file

    Raises:
        ValueError: if file is empty
        e: empty file

    Returns:
        ConfigBox
    """
    try:
        with open(path_to_yaml , 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded succefully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('File is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(directory_paths: list, verbose:bool = True ):
    """
    Create directories at paths mentioned in the list

    Args:
        directory_paths: List of path directories
        verbose: logs the creted files is set True
    """
    for path in directory_paths:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f'Created Director at: {path}')

@ensure_annotations
def get_size(file_path: str) -> str:
    """
    Returns size of file

    Args:
        file_path: path to a file

    Returns:
        Size of file in KB string 
    """
    size_in_KB = round(os.path.getsize(file_path)/ 1024)
    return f'~ {size_in_KB} KB'