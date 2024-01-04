from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_injestion import DataInjestion

class DataInjestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):   
        config_manager = ConfigManager()
        data_injestion_config = config_manager.get_data_injestion_config()
        data_injestion = DataInjestion(data_injestion_config)
        data_injestion.download_files()
        data_injestion.extract_zip_file()