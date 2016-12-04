import numpy as np
import json

import os
rootdir = 'data/raw/'

path='data/raw/'
rows=0

for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        rows += 1

X = np.zeros((rows,4))
y = np.zeros((rows))

row=0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".1") or file.endswith(".0"):
            with open(rootdir+file) as data_file:
                data = json.load(data_file)

                #Minimum Temperature
                X[row,0] = data['daily']['data'][0]['temperatureMin']
                #Probability
                X[row,1] = data['daily']['data'][0]['precipProbability']
                #Intensity
                X[row,2] = data['daily']['data'][0]['precipIntensity']
                #Accumulation
                if 'precipAccumulation' in data['daily']['data'][0]:
                    X[row,3] = data['daily']['data'][0]['precipAccumulation']
                else:
                    X[row,3] = 0

                #Build the Index array based on
                if file.endswith(".1"):
                    y[row] = 1
                if file.endswith(".0"):
                    y[row] = 0
                row=row+1

np.save("data/processed/data",X)
np.save("data/processed/index",y)
