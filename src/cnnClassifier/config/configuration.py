"""
Configuration Manager class
"""

from pathlib import Path
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig,
                                                PrepareCallbacksConfig,
                                                TrainingConfig,
                                                EvaluationConfig)



class ConfigurationManager:
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
            local_data_file = Path(config.local_data_file),
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

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        """
        Returns PrepareCallbacksConfig object
        """
        create_directories([Path(self.config.prepare_callbacks.root_dir),
                            Path(self.config.prepare_callbacks.tensorboard_root_log_dir),
                            Path(self.config.prepare_callbacks.checkpoint_model_filepath)])
        return PrepareCallbacksConfig(
            root_dir = Path(self.config.prepare_callbacks.root_dir),
            tensorboard_root_log_dir = Path(self.config.prepare_callbacks.tensorboard_root_log_dir),
            checkpoint_model_filepath= Path(self.config.prepare_callbacks.checkpoint_model_filepath)
        )

    def get_training_config(self) -> TrainingConfig:
        """
        Returns TrainingConfig object
        """
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = self.config.data_ingestion.unzip_dir
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=str(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config

    def get_validation_config(self) -> EvaluationConfig:
        """
        Returns EvaluationConfig object
        """
        eval_config = EvaluationConfig(
            path_of_model=Path("artifacts/training/model.keras"),
            training_data=Path("artifacts/data_ingestion/Chicken-Disease-Dataset"),
            params_batch_size=self.params.BATCH_SIZE,
            params_image_size=self.params.IMAGE_SIZE,
            all_params=self.params
        )
        return eval_config
