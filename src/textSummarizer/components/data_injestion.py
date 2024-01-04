import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataInjestionConfig
from pathlib import Path

class DataInjestion:
    """
    Performs Data Injestion Functions
    """
    def __init__(self, config:DataInjestionConfig):
        self.config = config

    def download_files(self):
        """
        Download Files from source_URL From Data Injestion Configuration
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded! with info: {headers}')
        else:
            logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        Extracts downloaded zip files and saves them to unzip_dir from Data Injestion Configuration
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
