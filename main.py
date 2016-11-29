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
    clf = svm.SVC(probability=True, kernel='rbf', tol=0.000000000001)
    clf.fit(X,y)

    try:
        os.remove('current.day')
    except OSError:
        pass

    url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806?exclude=currently,minutely,alerts,flags"
    file = wget.download(url, out="current.day")

    print("")

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

        # if 'precipType' in data['daily']['data'][dayfrom]:
        #     precipStr = data['daily']['data'][0]['precipType']
        #     if precipStr == 'snow':
        #         X[0,4] = 100
        #     if precipStr == 'rain':
        #         X[0,4] = 50
        # else:
        #     X[0,4] = 0
#BUILD VARIABLES TO PASS TO TEMPLATE
    #Percent Snowday for 3 Days
    resultArr = clf.predict_proba(prediction)
    final = str(resultArr.item((0,1))*100)

#RENDER TEMPLATE
    return render_template('index.html', final=final)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
