from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataInjestionConfig, DataValidationConfig, \
    DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
import os

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
    
    def get_data_validation_config(self)-> DataValidationConfig:
        """
        Return Data validation configuration
        """
        data_validation_config = DataValidationConfig(
            self.config.data_validation.root_dir,
            self.config.data_validation.status_file,
            self.config.data_validation.all_required_files,
            os.path.join(self.config.data_ingestion.root_dir, 
                         self.config.dataset_name+'_dataset')
        )
        return data_validation_config
    
    def get_data_transformation_config(self) ->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            dataset_path= self.config.data_ingestion.root_dir +'/' \
                         +self.config.dataset_name+'_dataset',
            tokenizer_name= config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = self.config.data_transformation.root_dir +'/' \
                         +self.config.dataset_name+'_dataset',
            tokenizer_name = self.config.data_transformation.tokenizer_name,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps  = params.gradient_accumulation_steps
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])
        model_eval_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            dataset_path= os.path.join(
                self.config.data_transformation.root_dir,
                self.config.dataset_name + '_dataset'),
            model_ckpt= os.path.join(self.config.model_trainer.root_dir, 'model'),
            tokenizer_path= os.path.join(self.config.model_trainer.root_dir, 'tokenizer'),
            metric_file_name  = config.metric_file_name
        )
        return model_eval_config