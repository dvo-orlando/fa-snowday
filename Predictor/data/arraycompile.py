import numpy as np
np.set_printoptions(threshold='nan')


a = np.load('trainingdata1.npy')
b = np.load('trainingdata2.npy')
c = np.load('trainingdata3.npy')
d = np.load('trainingdata4.npy')
e = np.load('trainingdata5.npy')
f = np.load('trainingdata6.npy')
g = np.load('trainingdata7.npy')
h = np.load('trainingdata8.npy')
i = np.load('trainingdata9.npy')
j = np.load('trainingdata10.npy')
k = np.load('trainingdata11.npy')
l = np.load('trainingdata12.npy')
m = np.load('trainingdata13.npy')

trainingdata = np.vstack((a,b,c,d,e,f,g,h,i,j,k,l,m))

np.save('trainingdata.npy',trainingdata)
