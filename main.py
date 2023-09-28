"""
Entry point for the application.
This module is responsible for calling the main method of the pipeline.
"""
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex


STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.error(ex, exc_info = True)
    raise ex


STAGE_NAME = "Model Training Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.exception(ex)
    raise ex

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
    evaluator = EvaluationPipeline()
    evaluator.main()
    logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
except Exception as ex:
    logger.exception(ex)
    raise ex
