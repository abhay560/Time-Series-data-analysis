import pandas as pd
from sqlalchemy import create_engine
from src.dataEngineer.entity.config_entity import DataLoadingConfig
from src.dataEngineer import logger
# DB CONNECTION
pwd = "Abhay%40"
DATABASE_URL = f"postgresql+psycopg2://postgres:{pwd}1999@localhost:5432/air_quality_db"
engine = create_engine(DATABASE_URL)



# RAW DATA LOADER
class DataLoading:

    def __init__(self, config = DataLoadingConfig):
        self.config = config

    def load_raw(self):
        """
        Load raw Air Quality CSV into air_quality_UCI.airquality_uci_raw
        """
        df = pd.read_csv(self.config.root_dir)

        expected_cols = [
            "Date", "Time", "CO(GT)", "PT08.S1(CO)", "NMHC(GT)", "C6H6(GT)",
            "PT08.S2(NMHC)", "NOx(GT)", "PT08.S3(NOx)", "NO2(GT)",
            "PT08.S4(NO2)", "PT08.S5(O3)", "T", "RH", "AH"
        ]
        df = df[expected_cols]

        # Load into Postgres
        with engine.begin() as conn:
            df.to_sql(
                "airquality_uci_raw",
                con=conn,
                schema="air_quality_uci",
                if_exists="append",
                index=False
            )
        logger.info(f"Loaded {len(df)} rows into air_quality_UCI.airquality_uci_raw")


# AGGREGATED METRICS LOADER
    def load_aggregates(self):
        """
        Load aggregated metrics CSV into air_quality_UCI.aggregated_metrics
        """
        df = pd.read_csv(self.config.metrics_dir)

        expected_cols = [
            "feature", "min_val", "max_val", "avg_val", "std_val",
            "source_file", "source_system"
        ]
        df = df[expected_cols]

        with engine.begin() as conn:
            df.to_sql(
                "aggregated_metrics",
                con=conn,
                schema="air_quality_uci",
                if_exists="append",
                index=False
            )
        logger.info(f"Loaded {len(df)} rows into air_quality_UCI.aggregated_metrics")
