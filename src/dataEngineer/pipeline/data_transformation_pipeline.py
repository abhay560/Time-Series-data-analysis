from src.dataEngineer.components.data_transformation import DataTransformation
from src.dataEngineer.config.configuration import ConfigurationManager
from src.dataEngineer import logger


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self, file_name):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config(file_name)
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.aggregated_metrices(file_name)


