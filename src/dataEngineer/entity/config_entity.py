from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict
    failed_data_dir: Path
    valid_data_dir: Path

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    metrics_dir: Path

@dataclass(frozen=True)
class DataLoadingConfig:
    root_dir: Path
    metrics_dir: Path