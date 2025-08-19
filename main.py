from pathlib import Path
import time
from src.dataEngineer.pipeline.data_loading_pipeline import DataLoadingPipeline
from src.dataEngineer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.dataEngineer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dataEngineer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.dataEngineer import logger

WATCH_DIR = Path("artifacts/data_ingestion")
raw_csv = "artifacts/data_ingestion/AirQualityUCI.csv"
agg_csv = "aggregated_metrics.csv"
CSV_SUFFIXES     = {".csv", ".CSV"}
seen: set[str] = set()
while True:
    
    try:
        for file in WATCH_DIR.glob("*"):
            if not file.is_file():
                continue
            if file.suffix not in CSV_SUFFIXES:
                continue
            if file.name in seen:
                continue


            STAGE_NAME = "Data Ingestion Stage"
            try:
                logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
                data_ingestion_pipeline = DataIngestionPipeline()
                data_ingestion_pipeline.main()
                seen.add(file.name)
                logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<")

            except Exception as e:
                logger.exception(e)
                raise e

            STAGE_NAME = "Data Validation Stage"
            try:
                logger.info(f">>>>> stage {STAGE_NAME} started <<<")
                data_validation_pipeline = DataValidationPipeline()
                data_validation_pipeline.main(file.name)
                seen.add(file.name)
                logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
                status = "artifacts/data_validation/status.txt"
                with open(status, 'r') as f:
                    content = f.read() 
                    status_value = content.split(":")[-1].strip()
                if status_value == "False":
                    continue

            except Exception as e:
                raise e

            STAGE_NAME = "Data Transformation Stage"
            try:
                logger.info(f">>>> stage {STAGE_NAME} started <<<<")
                data_transformation_pipeline = DataTransformationPipeline()
                data_transformation_pipeline.main(file.name)
                seen.add(file.name)
                logger.info(f">>>> stage {STAGE_NAME} completed <<<<<")

            except Exception as e:
                logger.info(e)
                seen.add(file.name)
                continue
                

            STAGE_NAME = "DATA LOADING START"


            try:
                logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
                data_loading_pipeline = DataLoadingPipeline()
                data_loading_pipeline.main(file.name)
                seen.add(file.name)
                logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

            except Exception as e:
                seen.add(file.name)
                logger.info(e)
                continue 
    except KeyboardInterrupt:
        break
    except Exception as e:
        logger.info(e)

    time.sleep(10)

