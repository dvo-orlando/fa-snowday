from flask import Flask
from flask import render_template
from sklearn import svm
import numpy as np
import wget
import json
import os

app = Flask(__name__)

@app.route("/")
def hello():

    execfile('data/getData.py')
    execfile('data/processData.py')

    #Load numpy arrays
    X = np.load('data/processed/data.npy')
    y = np.load('data/processed/index.npy')

    #Convert "y" to compatible array
    y = y.ravel()

    #Create and fit Support Vector Machine
    clf = svm.SVC(probability=True, kernel='linear', tol=0.001, C=0.95, class_weight='balanced')
    clf.fit(X,y)

    try:
        os.remove('current.day')
    except OSError:
        pass

    url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806?exclude=currently,hourly,minutely,alerts,flags"
    file = wget.download(url, out="current.day")

    prediction = np.zeros((1,4))

    dayfrom=1
    with open("current.day") as data_file:
        data = json.load(data_file)

        prediction[0,0] = data['daily']['data'][dayfrom]['temperatureMin']
        prediction[0,1] = data['daily']['data'][dayfrom]['precipProbability']
        prediction[0,2] = data['daily']['data'][dayfrom]['precipIntensity']
        if 'precipAccumulation' in data['daily']['data'][dayfrom]:
            prediction[0,3] = data['daily']['data'][dayfrom]['precipAccumulation']
        else:
            prediction[0,3] = 0


    prediction2 = np.zeros((1,4))

    dayfrom=2
    with open("current.day") as data_file:
        data = json.load(data_file)

        prediction2[0,0] = data['daily']['data'][dayfrom]['temperatureMin']
        prediction2[0,1] = data['daily']['data'][dayfrom]['precipProbability']
        prediction2[0,2] = data['daily']['data'][dayfrom]['precipIntensity']
        if 'precipAccumulation' in data['daily']['data'][dayfrom]:
            prediction2[0,3] = data['daily']['data'][dayfrom]['precipAccumulation']
        else:
            prediction2[0,3] = 0

    prediction3 = np.zeros((1,4))

    dayfrom=3
    with open("current.day") as data_file:
        data = json.load(data_file)

        prediction3[0,0] = data['daily']['data'][dayfrom]['temperatureMin']
        prediction3[0,1] = data['daily']['data'][dayfrom]['precipProbability']
        prediction3[0,2] = data['daily']['data'][dayfrom]['precipIntensity']
        if 'precipAccumulation' in data['daily']['data'][dayfrom]:
            prediction3[0,3] = data['daily']['data'][dayfrom]['precipAccumulation']
        else:
            prediction3[0,3] = 0

#ORGANIZE VARIABLES TO PASS TO TEMPLATE
    resultArr = clf.predict_proba(prediction)
    resultArr2 = clf.predict_proba(prediction2)
    resultArr3 = clf.predict_proba(prediction3)
    final = str(resultArr.item((0,1))*100)
    final2 = str(resultArr2.item((0,1))*100)
    final3 = str(resultArr3.item((0,1))*100)

#RENDER TEMPLATE
    return render_template('index.html', final=final, final2=final2, final3=final3)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
