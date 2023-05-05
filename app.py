import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    output = round(prediction[0],1)

    return render_template("index.html", prediction_text = "The Sales with advertising will be $ {}".format(output))

if __name__ == "__main__":
    app.run(port=5000,debug=True)