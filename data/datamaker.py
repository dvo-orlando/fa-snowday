import numpy as np
import json

# FIND NUMBER OF JSON FILES
rows=0

import os
rootdir = '/home/dominic/Work/snowday/Predictor/data/raw/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".snowday") or file.endswith(".day"):
            rows=rows+1

X = np.zeros((rows,14))
y = np.zeros((rows,1))

row=0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".snowday") or file.endswith(".day"):
            with open(file) as data_file:
                data = json.load(data_file)

                X[row,0] = data['daily']['data'][0]['moonPhase']
                X[row,1] = data['daily']['data'][0]['precipIntensity']
                X[row,2] = data['daily']['data'][0]['precipIntensityMax']
                X[row,3] = data['daily']['data'][0]['precipProbability']
                X[row,4] = data['daily']['data'][0]['temperatureMin']
                X[row,5] = data['daily']['data'][0]['temperatureMax']
                X[row,6] = data['daily']['data'][0]['apparentTemperatureMin']
                X[row,7] = data['daily']['data'][0]['apparentTemperatureMax']
                X[row,8] = data['daily']['data'][0]['dewPoint']
                X[row,9] = data['daily']['data'][0]['humidity']
                X[row,10] = data['daily']['data'][0]['windSpeed']
                X[row,11] = data['daily']['data'][0]['windBearing']
                X[row,12] = data['daily']['data'][0]['visibility']
                X[row,13] = data['daily']['data'][0]['pressure']

                if file.endswith(".snowday"):
                    y[row,0] = 1
                if file.endswith(".day"):
                    y[row,0] = 0

                row=row+1


np.save("processed/data",X)
np.save("processed/index",y)
