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
    