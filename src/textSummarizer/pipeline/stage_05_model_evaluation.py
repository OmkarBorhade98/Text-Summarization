from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config_manager = ConfigManager()
            model_evaluation_config = config_manager.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.evaluate()
        except Exception as e:
            raise e