"""
This module contains the PrepareCallback class, which is used to create 
callbacks for the model training process.
"""
import os
import time
import tensorflow as tf # to call VGG16 from keras
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig


class PrepareCallback:
    """
    PrepareCallback class   
    """

    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        """
        Creates TensorBoard Callbacks
        """
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)


    @property
    def _create_ckpt_callbacks(self):
        """	
        Creates Model Checkpoint Callbacks    
        """
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=str(self.config.checkpoint_model_filepath),
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        """
        Returns TensorBoard and Checkpoint callbacks
        """
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
