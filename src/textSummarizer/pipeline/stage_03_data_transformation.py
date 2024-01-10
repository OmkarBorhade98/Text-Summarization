from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_tranformation import DataTranformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigManager()
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation = DataTranformation(data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e