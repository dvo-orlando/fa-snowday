from sklearn import svm
import numpy as np
import wget
import json

X = np.load('data/raw/data.npy')
y = np.load('data/raw/index.npy')
y=y.ravel()
print(y)
# print(X)
# print(y)
#Training Data

#Known "solutions"

clf = svm.SVC()
clf.fit(X,y)


# print("Support Vectors: ")
# print(clf.support_vectors_)
#
# print("Indices of Support Vectors: ")
# print(clf.support_)

#get current data and predict
url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806?exclude=currently,minutely,hourly,alerts,flags"
file = wget.download(url, out="current.day")

prediction = np.zeros((1,14))
with open("44.0165,-70.9806") as data_file:
    data = json.load(data_file)
    prediction[0,0] = data['daily']['data'][1]['moonPhase']
    prediction[0,1] = data['daily']['data'][1]['precipIntensity']
    prediction[0,2] = data['daily']['data'][1]['precipIntensityMax']
    prediction[0,3] = data['daily']['data'][1]['precipProbability']
    prediction[0,4] = data['daily']['data'][1]['temperatureMin']
    prediction[0,5] = data['daily']['data'][1]['temperatureMax']
    prediction[0,6] = data['daily']['data'][1]['apparentTemperatureMin']
    prediction[0,7] = data['daily']['data'][1]['apparentTemperatureMax']
    prediction[0,8] = data['daily']['data'][1]['dewPoint']
    prediction[0,9] = data['daily']['data'][1]['humidity']
    prediction[0,10] = data['daily']['data'][1]['windSpeed']
    prediction[0,11] = data['daily']['data'][1]['windBearing']
    prediction[0,12] = data['daily']['data'][1]['visibility']
    prediction[0,13] = data['daily']['data'][1]['pressure']



print(prediction)

clf.predict(prediction)
