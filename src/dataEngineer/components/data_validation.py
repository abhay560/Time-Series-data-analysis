import shutil
import pandas as pd
from src.dataEngineer.entity.config_entity import DataValidationConfig
from src.dataEngineer import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            data = data[[c for c in data.columns if not str(c).startswith("Unnamed")]]

            expected_dtype = self.config.all_schema
            data_dtype = dict(data.dtypes)

            for col, exp in data_dtype.items():
                if col not in expected_dtype.keys():
                    validation_status = False
                    shutil.move(self.config.unzip_data_dir, self.config.failed_data_dir)
                    logger.info(f"Extra column found in dataset at {self.config.unzip_data_dir} and moved to {self.config.failed_data_dir}")
                    break
                data_type = expected_dtype[col]  
                if  str(data_type) != str(exp):
                    validation_status = False
                    shutil.move(self.config.unzip_data_dir, self.config.failed_data_dir)
                    logger.info(f"Extra column found in dataset at {self.config.unzip_data_dir} and moved to {self.config.failed_data_dir}")
                    break
                    
                else:
                    validation_status = True
            if validation_status == True:
                shutil.move(self.config.unzip_data_dir, self.config.valid_data_dir)
                logger.info(f"Data is Valid, moved to {self.config.valid_data_dir} and ready to use for further processing")
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
                f.close()


            return validation_status
        except Exception as e:
            raise e        
            