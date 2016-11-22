import os
from flask import Flask

app = Flask(__name__)


#predictor
from sklearn import svm
import numpy as np
import wget
import json
import os

#Load numpy arrays
X = np.load('data/raw/data.npy')
y = np.load('data/raw/index.npy')

#Convert "y" to compatible type
y = y.ravel()

#Create and fit Support Vector Machine
clf = svm.SVC()
clf.fit(X,y)


@app.route("/")
def hello():
    try:
        os.remove('current.day')
    except OSError:
        pass

    url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806?exclude=currently,minutely,hourly,alerts,flags"
    file = wget.download(url, out="current.day")

    print("")

    prediction = np.zeros((1,14))

    dayfrom = 1

    with open("current.day") as data_file:
        data = json.load(data_file)
        prediction[0,0] = data['daily']['data'][dayfrom]['moonPhase']
        prediction[0,1] = data['daily']['data'][dayfrom]['precipIntensity']
        prediction[0,2] = data['daily']['data'][dayfrom]['precipIntensityMax']
        prediction[0,3] = data['daily']['data'][dayfrom]['precipProbability']
        prediction[0,4] = data['daily']['data'][dayfrom]['temperatureMin']
        prediction[0,5] = data['daily']['data'][dayfrom]['temperatureMax']
        prediction[0,6] = data['daily']['data'][dayfrom]['apparentTemperatureMin']
        prediction[0,7] = data['daily']['data'][dayfrom]['apparentTemperatureMax']
        prediction[0,8] = data['daily']['data'][dayfrom]['dewPoint']
        prediction[0,9] = data['daily']['data'][dayfrom]['humidity']
        prediction[0,10] = data['daily']['data'][dayfrom]['windSpeed']
        prediction[0,11] = data['daily']['data'][dayfrom]['windBearing']
        prediction[0,12] = data['daily']['data'][dayfrom]['visibility']
        prediction[0,13] = data['daily']['data'][dayfrom]['pressure']


    if clf.predict(prediction) == [ 0.]:
        yesno = "Tomorrow will not be a snowday."
    if clf.predict(prediction) == [ 1.]:
        yesno = "Tomorrow will be a snowday."

    return yesno

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
