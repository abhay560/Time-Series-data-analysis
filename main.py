from src.dataEngineer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dataEngineer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.dataEngineer import logger




STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started <<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started <<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<")

except Exception as e:
    raise e