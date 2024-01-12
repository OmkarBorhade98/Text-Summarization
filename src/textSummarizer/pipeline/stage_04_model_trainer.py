from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e