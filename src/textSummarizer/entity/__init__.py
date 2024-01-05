from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataInjestionConfig:
    """
    A Data Injestion Configuration Data Class.
    
    Data:
        root_dir: Root DDirectory
        source_URL: Source Url form where Data is to be downloaded
        local_data_file: Path where Downloaded Data will be stored
        unzip_dir: Path where downloaded data will be unzipped and stored
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen= True)
class DataValidationConfig:
    """
    A Data Validation Data Class
    Data:
        root_dir: Root Directory
        status_file: Path to status file
        all_required_files: List of required files
        dataset_dir: path to dataset (gotten from data ingestion)
    """
    root_dir: Path
    status_file: str
    all_required_files: list
    dataset_dir: str