"""
Entry point for the application.
This module is responsible for calling the main method of the pipeline.
"""
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex
