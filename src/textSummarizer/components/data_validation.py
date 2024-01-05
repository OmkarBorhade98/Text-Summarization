from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig
from textSummarizer.utils.common import create_directories
import os

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def validate_all_files(self)-> bool:
        try:
            all_files = os.listdir(self.config.dataset_dir)
            for file in all_files:
                    validation_status = True
                    if file not in self.config.all_required_files:
                        validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
             raise e