from pathlib import Path
import time
from src.dataEngineer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.dataEngineer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dataEngineer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.dataEngineer import logger

WATCH_DIR = Path("artifacts/data_ingestion")
CSV_SUFFIXES     = {".csv", ".CSV"}
monitoring_time = 5
already_checked_files: set[str] = set()

while True:
    try:
        for file in WATCH_DIR.glob("*"):
            if not file.is_file():
                continue
            if file.suffix not in CSV_SUFFIXES:
                continue
            if file.name in already_checked_files:
                continue


            STAGE_NAME = "Data Ingestion Stage"
            try:
                logger.info(f"---------- Stage {STAGE_NAME} started ----------")
                data_ingestion_pipeline = DataIngestionPipeline()
                data_ingestion_pipeline.main()
                already_checked_files.add(file.name)
                logger.info(f"---------- Stage {STAGE_NAME} completed ----------")

            except Exception as e:
                logger.exception(e)
                raise e

            STAGE_NAME = "Data Validation Stage"
            try:
                logger.info(f"---------- Stage {STAGE_NAME} started ----------")
                data_validation_pipeline = DataValidationPipeline()
                data_validation_pipeline.main(file.name)
                already_checked_files.add(file.name)
                logger.info(f"---------- Stage {STAGE_NAME} completed ----------")
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
                logger.info(f"---------- Stage {STAGE_NAME} started ----------")
                data_transformation_pipeline = DataTransformationPipeline()
                data_transformation_pipeline.main(file.name)
                already_checked_files.add(file.name)
                logger.info(f"---------- Stage {STAGE_NAME} completed ----------")

            except Exception as e:
                logger.info(e)
                already_checked_files.add(file.name)
                continue
                

            STAGE_NAME = "DATA LOADING"


            try:
                logger.info(f"---------- Stage {STAGE_NAME} started ----------")
                '''data_loading_pipeline = DataLoadingPipeline()
                data_loading_pipeline.main(file.name)
                already_checked_files.add(file.name)'''
                logger.info("Please make Database connections, if you want to store the data to database")
                logger.info(f"---------- Stage {STAGE_NAME} completed ----------")

            except Exception as e:
                already_checked_files.add(file.name)
                logger.info(e)
                continue 
    except KeyboardInterrupt:
        break
    except Exception as e:
        logger.info(e)

    time.sleep(monitoring_time)

