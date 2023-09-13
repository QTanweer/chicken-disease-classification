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
