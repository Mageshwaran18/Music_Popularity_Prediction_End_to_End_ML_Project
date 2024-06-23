from src.Music_Popularity_Prediction_End_to_End_ML_Project.config import configuration
from src.Music_Popularity_Prediction_End_to_End_ML_Project import logger
from src.Music_Popularity_Prediction_End_to_End_ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e