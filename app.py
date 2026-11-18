'''
This (''' ''') is used to explain the overview of the project. 
'''

import flask
from flask import Flask,render_template,request
import numpy as np
import pickle
app = Flask(__name__)

with open("SLR_MODEL.pkl" , "rb") as f:
    model = pickle.load(f)

@app.route("/")
def default_site():
    return render_template("index.html")

@app.route("/predict",methods = ['GET','POST'])
def prediction():
    if request.method == "POST":
        value = [float(i) for i in request.form.values()]
        value = np.array([value])
        result = model.predict(value)[0]
        return render_template("index.html" , result = result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)