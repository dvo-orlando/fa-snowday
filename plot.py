from flask import Flask
from flask import render_template
from sklearn import svm
import numpy as np
import wget
import json
import os

#plotting imports
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")


execfile('data/getData.py')
execfile('data/processData.py')

#Load numpy arrays
X = np.load('data/processed/data.npy')
y = np.load('data/processed/index.npy')

#Convert "y" to compatible array
y = y.ravel()

#normalize values
graphX = X / X.max(axis=0)


#Create and fit Support Vector Machine
clf = svm.SVC(probability=True, kernel='linear', tol=0.001, C=0.95, class_weight='balanced')
clf.fit(X,y)



#plot
w = clf.coef_[0]
print(w)

a = -w[0] / w[1]


cm = ListedColormap(['#0000FF','#FF0000'])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(graphX[:,0], graphX[:,1], graphX[:,3], c=y, marker='o', cmap=cm)

ax.set_xlabel('temp')
ax.set_ylabel('probability')
ax.set_zlabel('accum')




try:
    os.remove('current.day')
except OSError:
    pass

url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806?exclude=currently,hourly,minutely,alerts,flags"
file = wget.download(url, out="current.day")

prediction0 = np.zeros((1,4))

dayfrom=0
with open("current.day") as data_file:
    data = json.load(data_file)

    prediction0[0,0] = data['daily']['data'][dayfrom]['temperatureMin']
    prediction0[0,1] = data['daily']['data'][dayfrom]['precipProbability']
    prediction0[0,2] = data['daily']['data'][dayfrom]['precipIntensity']
    if 'precipAccumulation' in data['daily']['data'][dayfrom]:
        prediction0[0,3] = data['daily']['data'][dayfrom]['precipAccumulation']
    else:
        prediction0[0,3] = 0

prediction1 = np.zeros((1,4))

dayfrom=1
with open("current.day") as data_file:
    data = json.load(data_file)

    prediction1[0,0] = data['daily']['data'][dayfrom]['temperatureMin']
    prediction1[0,1] = data['daily']['data'][dayfrom]['precipProbability']
    prediction1[0,2] = data['daily']['data'][dayfrom]['precipIntensity']
    if 'precipAccumulation' in data['daily']['data'][dayfrom]:
        prediction1[0,3] = data['daily']['data'][dayfrom]['precipAccumulation']
    else:
        prediction1[0,3] = 0


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
resultArr0 = clf.predict_proba(prediction0)
resultArr1 = clf.predict_proba(prediction1)
resultArr2 = clf.predict_proba(prediction2)
resultArr3 = clf.predict_proba(prediction3)
final0 = str(resultArr0.item((0,1))*100)
final1 = str(resultArr1.item((0,1))*100)
final2 = str(resultArr2.item((0,1))*100)
final3 = str(resultArr3.item((0,1))*100)


print "probability" + final0


plt.show()
