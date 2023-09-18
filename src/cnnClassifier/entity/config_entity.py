'''
Entity class for DataIngestionConfig 

'''
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestionConfig Entity class
    """
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """
    PrepareBaseModelConfig Entity class
    """
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_include_top: bool
    params_weights: str
    params_classes: int
    params_learning_rate: float

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    """
    PrepareCallbacksConfig Entity class
    """
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
