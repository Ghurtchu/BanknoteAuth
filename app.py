import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, redirect
from flasgger import Swagger
from constants import *

app = Flask(__name__)
Swagger(app)

with open('classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)


@app.route(DEFAULT_ENDPOINT, methods=[METHOD_GET])
def home_page():
    return redirect(DEFAULT_PATH)


@app.route(PREDICT_ENDPOINT, methods=[METHOD_GET])
def predict_note_authentication():
    """
    Authenticate the BankNote by supplying query parameters
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
          200:
              description: The output values
    """
    variance = request.args.get(VARIANCE)
    skewness = request.args.get(SKEWNESS)
    curtosis = request.args.get(CURTOSIS)
    entropy = request.args.get(ENTROPY)
    feature_vector = np.array([variance, skewness, curtosis, entropy]).reshape(1, -1)
    prediction = classifier.predict(feature_vector)
    return decode_predicted_value(prediction[0])


@app.route(PREDICT_FILE_ENDPOINT, methods=[METHOD_POST])
def predict_note_authentication_file():
    """
    Authenticate the BankNote by supplying .csv file
    ---
    parameters:
        - name: .csv file
          in: formData
          type: file
          required: true
    responses:
          200:
              description: The output values
    """
    df_test = pd.read_csv(request.files.get(CSV_FILE))
    predictions = classifier.predict(df_test)
    return 'predicted values for the csv are ' + str(
        list([decode_predicted_value(predicted_value) for predicted_value in predictions]))


def decode_predicted_value(predicted_value):
    return CLASS_1 if predicted_value == 1 else CLASS_0


if __name__ == MAIN:
    app.run(host=LOCALHOST, port=FLASK_APP_PORT, debug=True, use_reloader=True)
