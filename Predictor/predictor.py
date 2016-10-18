from sklearn import svm


#Training Data
X = [[ 32 , 50 ]  ,  [22 , 80 ] , [ 50 , 20] , [33,20]]

#Known "solutions"
y = [1,1,0,0]

clf = svm.SVC()
clf.fit(X,y)


print("Support Vectors: ")
print(clf.support_vectors_)

print("Indices of Support Vectors: ")
print(clf.support_)


print("Prediction: ")
print(clf.predict([[data["hourly_forecast"][0]["temp"]["english"],data["hourly_forecast"][0]["humidity"]]]))
