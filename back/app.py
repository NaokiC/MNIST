import base64
from typing import io
from io import BytesIO
import flask
import requests
import PIL.Image
from flask import Flask, request
import json
from ai import Ai
from flask_cors import cross_origin, CORS

# Creating Flask server
app = Flask(__name__)

# Allowing all origins for Cors Policy
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

# POST request for prediction
@app.route('/', methods=['POST'])
def predict():
    # Getting the data transmitted in a JSON by the POST request
    parameters = request.get_json(force=True)

    # Creating the AI
    ai = Ai()

    # Checking if the POST request was made from Postman
    if str(parameters['image'])[0] == '/':
        predicted_value: int = ai.predict(parameters['image'], True)
    else:
        # Collecting image from JSON
        picture_request = str(parameters['image'])
        starter = picture_request.find(',')
        image_data = picture_request[starter + 1:]
        image_data = bytes(image_data, encoding="ascii")

        # The image has been transferred encoded in base64 model, the line just below decode it and create an image form it
        with open('./assets/image.jpeg', 'wb') as fh:
            fh.write(base64.decodebytes(image_data))

        # Launching the prediction
        predicted_value: int = ai.predict("./assets/image.jpeg", True)

    # Creating the data for the JSON file to be returned
    data_set = {
        "image": {
            "name": parameters['image'],
            "reshaped size": "28*28",
            "color scale": "grey scale"
        },
        "Multi-Layers Perceptron spec": {
            "hidden_layer_sizes": "(200,)",
            "activation": "logistic",
            "alpha": "1e-4",
            "solver": "sgd",
            "tol": "1e-4",
            "random_state": 2,
            "max_iter": 200,
            "learning_rate_init": .0001,
            "verbose": "True"
        },
        "ML algorithm score on NMIST digits": {
            "time": "0:05:53",
            "accuracy score on training data": "0.960970871012443"
        },
        "Predicted value": predicted_value
    }

    # Creating the JSON
    json_to_be_returned = json.dumps(data_set)

    # Returning the JSON
    return json_to_be_returned


if __name__ == '__main__':
    app.run(host='0.0.0.0')
