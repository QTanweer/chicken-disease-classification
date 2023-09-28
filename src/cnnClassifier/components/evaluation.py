"""	
Evaluation Component
"""
from pathlib import Path
import tensorflow as tf
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json


class Evaluation:
    """
    Evaluation Component
    """
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.score = None
        self.valid_generator = None

    def _valid_generator (self):

        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path_of_model : Path):
        """
        Loads the model
        """

        return tf.keras.models.load_model(path_of_model)

    def evaluation(self):
        """
        Evaluates the model
        """
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator, verbose=1)

    def save_score(self):
        """
        Saves the score
        """
        scores = {
            "loss" : self.score[0],
            "accuracy" : self.score[1]
            }
        save_json(path=Path("scores.json"), data=scores)
