"""
Configuration Manager class
"""

from pathlib import Path
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


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
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # print(f"Configs: {self.config}")
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns DataIngestionConfig object
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Returns PrepareBaseModelConfig object
        """
        create_directories([self.config.prepare_base_model.root_dir])
        return PrepareBaseModelConfig(
            root_dir = Path(self.config.prepare_base_model.root_dir),
            base_model_path = Path(self.config.prepare_base_model.base_model_path),
            updated_base_model_path= Path(self.config.prepare_base_model.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES,
            params_learning_rate = self.params.LEARNING_RATE
        )
    