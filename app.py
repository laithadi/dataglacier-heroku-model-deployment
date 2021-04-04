import numpy as np
import pickle
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods= ["POST"])
def predict():

    features = [int(x) for x in request.form.values()]
    features = [np.array(features)]
    prediction = model.predict(features)

    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text= "House price should be $ {}".format(output))


if __name__ == "__main__":
    app.run(debug = True)


