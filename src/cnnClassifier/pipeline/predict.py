import numpy as np
from pathlib import Path 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import os


class PredictionPipeline:
    """
    Pipeline for predicting the class of an image
    """
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        """
        Make a prediction based on the image
        """
        model = load_model(Path("artifacts/training/model.keras"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{"image": prediction}]

        else:
            prediction = 'Coccdiosis'
            return [{"image": prediction}]
                           