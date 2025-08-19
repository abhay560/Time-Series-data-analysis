from src.db.load_data import DataLoading
from src.dataEngineer.config.configuration import ConfigurationManager


class DataLoadingPipeline:
    def __init__(self):
        pass

    def main(self, file_name):
        config = ConfigurationManager()
        data_loading_config = config.get_data_loading_config(file_name)
        data_loading = DataLoading(config = data_loading_config)
        data_loading.load_raw()
        data_loading.load_aggregates()
        
