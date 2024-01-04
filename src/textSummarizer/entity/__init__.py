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