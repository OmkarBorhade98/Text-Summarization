from textSummarizer.pipeline.stage_01_data_injestion import DataInjestionTrainingPipeline
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