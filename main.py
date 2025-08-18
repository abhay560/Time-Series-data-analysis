from src.db.load_data import DataLoading
from src.dataEngineer.pipeline.data_transformation_pipeline import DataTransformationPipeline
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

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    raise e

STAGE_NAME = "DATA LOADING START"
raw_csv = "artifacts/data_ingestion/AirQualityUCI.csv"
agg_csv = "aggregated_metrics.csv"
try:
    logger.info(f">>>>>stage {STAGE_NAME} started <<<<<")
    data_loading = DataLoading()
    data_loading.load_raw(raw_csv)
    data_loading.load_aggregates(agg_csv)
except Exception as e:
    raise e

