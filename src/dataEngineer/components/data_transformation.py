

from pathlib import Path
import shutil
import pandas as pd
from src.dataEngineer.entity.config_entity import DataTransformationConfig
from src.dataEngineer import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def aggregated_metrices(self, file_name):
        if Path(self.config.data_path).is_file():
            try:
                data = pd.read_csv(self.config.data_path)
                data["timestamp"] = pd.to_datetime(
                data["Date"].astype(str) + " " + data["Time"].astype(str),
                dayfirst=True,
                errors="coerce",
                utc=True
                )
                source_system = "kaggle_airquality_uci"
                data = data.drop(columns=["Date","Time"])
                numeric_cols = data.select_dtypes(include="number").columns
                aggregated_metrics = data[numeric_cols].agg(["min","max","mean","std"]).T.reset_index()
                aggregated_metrics.columns = ["feature","min_val","max_val","avg_val","std_val"]
                aggregated_metrics["source_file"] = "AirQuality.csv"
                aggregated_metrics["source_system"] = "kaggle_airquality_uci"
                aggregated_metrics_file = f"aggregated_metrics_{file_name}"
                aggregated_metrics.to_csv(aggregated_metrics_file, index = False)
                shutil.move(aggregated_metrics_file, self.config.metrics_dir )
                logger.info(f"Data has been processed from {source_system} in file {file_name}")

            except Exception as e:
                raise e
        else:
            logger.info(f"Valid Data file is not present at {self.config.data_path}")

    
        
        