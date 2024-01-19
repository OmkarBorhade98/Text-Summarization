from textSummarizer.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME ='Data Injestion'
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataInjestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME ='Data Validation'
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Data Tranformation'
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      data_tranformation = DataTransformationTrainingPipeline()
      data_tranformation.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      raise e

STAGE_NAME = 'Model Trainer'
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      model_trainer = ModelTrainerTrainingPipeline()
      model_trainer.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      raise e

STAGE_NAME = 'Model Evaluation'
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      model_evaluation = ModelEvaluationTrainingPipeline()
      model_evaluation.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      raise e