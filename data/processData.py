import numpy as np
import json

import os
rootdir = 'data/raw/'

path='data/raw/'
rows=0

for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        rows += 1

X = np.zeros((rows,13))
y = np.zeros((rows,1))

row=0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".1") or file.endswith(".0"):
            with open(rootdir+file) as data_file:
                data = json.load(data_file)

                X[row,0] = data['daily']['data'][0]['precipIntensity']
                X[row,1] = data['daily']['data'][0]['precipIntensityMax']
                X[row,2] = data['daily']['data'][0]['precipProbability']
                X[row,3] = data['daily']['data'][0]['temperatureMin']
                X[row,4] = data['daily']['data'][0]['temperatureMax']
                X[row,5] = data['daily']['data'][0]['apparentTemperatureMin']
                X[row,6] = data['daily']['data'][0]['apparentTemperatureMax']
                X[row,7] = data['daily']['data'][0]['dewPoint']
                X[row,8] = data['daily']['data'][0]['humidity']
                X[row,9] = data['daily']['data'][0]['windSpeed']
                X[row,10] = data['daily']['data'][0]['windBearing']
                X[row,11] = data['daily']['data'][0]['visibility']
                X[row,12] = data['daily']['data'][0]['pressure']

                if file.endswith(".1"):
                    y[row,0] = 1
                if file.endswith(".0"):
                    y[row,0] = 0

                row=row+1


np.save("data/processed/data",X)
np.save("data/processed/index",y)
