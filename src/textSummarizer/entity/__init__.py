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


@dataclass(frozen = True)
class DataTransformationConfig:
    """
    A Data Transformation Data Class
    Data:
        root_dir: Root Directory
        dataset_path: Local Dataset Path
        tokenizer_name: Tokenizer to be used
    """
    root_dir: Path
    dataset_path: Path
    tokenizer_name: Path

@dataclass(frozen= True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    tokenizer_name: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen= True)
class ModelEvaluationConfig:
    root_dir: Path
    dataset_path: Path
    model_ckpt: Path
    tokenizer_path: Path
    metric_file_name: Path