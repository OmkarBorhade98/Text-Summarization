from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataInjestionConfig

class ConfigManager:
    """
    Manages model configuration
    """
    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])
    
    def get_data_injestion_config(self)->DataInjestionConfig:
        """
        Returns Data Injestion Configuration
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_injestion_config = DataInjestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_injestion_config