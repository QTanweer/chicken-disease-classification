"""
Configuration Manager class
"""

from pathlib import Path
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfiguratonManager:
    """
    Configuration Manager class
    """
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            ):
        print("Configuration Manager Initiated")
        # print(f"Config File Path: {config_filepath}, with dtype {type(config_filepath)}")
        # print(f"Params File Path: {params_filepath} with dtype {type(params_filepath)}")
        self.configs = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # print(f"Configs: {self.configs}")
        create_directories([self.configs.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns DataIngestionConfig object
        """
        config = self.configs.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

# config_dummy = ConfiguratonManager()
