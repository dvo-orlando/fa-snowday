#import data
import json
from pprint import pprint

with open('sample_data/samplejson_hourly.json') as data_file:
    data = json.load(data_file)


#prints data
    #pprint(data)


#Example for accessing the hour of the first "hourly_forecast" object array,
    #print(data["hourly_forecast"][0]["FCTTIME"]["hour"])


from sklearn import svm

X = [[ 32 , 50 ]  ,  [22 , 80 ] , [ 50 , 20] , [33,20]]
y = [1,1,0,0]

clf = svm.SVC()
clf.fit(X,y)


print("Support Vectors: ")
print(clf.support_vectors_)

print("Indices of Support Vectors: ")
print(clf.support_)


print("Prediction: ")
print(clf.predict([[data["hourly_forecast"][0]["temp"]["english"],data["hourly_forecast"][0]["humidity"]]]))
