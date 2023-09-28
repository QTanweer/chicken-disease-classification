"""
This is the main file for the flask app
"""
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decode_image
from cnnClassifier.pipeline.predict import PredictionPipeline


app = Flask(__name__)
cors = CORS(app)

class ClientApp:
    """
    ClientApp class for predicting the class of an image
    """
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(filename=self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    """
    return: returns the home page
    """
    return render_template('index.html')

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def train_route():
    """
    return: returns the training page
    """
    os.system("dvc repro")
    return "Model Trained Successfully"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predict_route():
    """
    return: returns the prediction page
    """
    image = request.json["image"]
    #client_app = ClientApp()
    decode_image(image, file_name=client_app.filename)
    result = client_app.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    client_app  = ClientApp()
    app.run(host = '0.0.0.0', port = 8080)
