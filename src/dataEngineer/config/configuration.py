import os
from src.dataEngineer.entity.config_entity import DataIngestionConfig, DataLoadingConfig, DataTransformationConfig, DataValidationConfig
from src.dataEngineer.utils.common import create_directories, read_yaml
from pathlib import Path
CONFIG_FILE_PATH = Path("config/config.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")


class ConfigurationManager:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self, file_name) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir, config.failed_data_dir, config.valid_data_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = os.path.join(config.unzip_data_dir, file_name),
            all_schema = schema,
            failed_data_dir = config.failed_data_dir,
            valid_data_dir = config.valid_data_dir
        )

        return data_validation_config
    

    def get_data_transformation_config(self, file_name) -> DataTransformationConfig:

        config = self.config.data_transformation
        create_directories([config.metrics_dir])
        self.prefixed_name = f"valid_data_{file_name}"

        data_transformation_config = DataTransformationConfig(
            data_path = Path(config.data_path) / self.prefixed_name,
            metrics_dir = config.metrics_dir

        )

        return data_transformation_config
    
    def get_data_loading_config(self, file_name) -> DataLoadingConfig:

        config = self.config.data_loading
        create_directories([config.root_dir, config.metrics_dir])
        self.prefixed_name = f"aggregated_metrics_{file_name}"

        data_loading_config = DataLoadingConfig(
            root_dir = Path(config.root_dir) / file_name,
            metrics_dir = Path(config.metrics_dir) / self.prefixed_name,
        )

        return data_loading_config



        
