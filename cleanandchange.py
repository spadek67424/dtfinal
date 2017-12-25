import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
data = pd.read_table("earthquake_UTF8.txt", encoding='utf-16')
eq_location = data.values

newframe=data.ix[:,4]
city=list()
distance=list()

datey=list()
timey=list()
depth=data.ix[:,2].values
mag=data.ix[:,3].values
for x in newframe:
	city.append(x[0:2])
	temp=x.split(" ")
	distance.append(float(temp[1]))    # city is city name , distance is distance between location and city

newframe=data.ix[:,1]
for x in newframe:
	temp=x.split(" ")
	datey.append(temp[0])
	timey.append(temp[1])

newframe={ 	"city":city,
			"distance":distance,
			"date":datey,
			"time":timey,
			"depth":depth,
			"magnitude":mag}
trynew=pd.DataFrame(newframe)


trynew2=trynew[::-1]
previousn=50 #50 if from paper, sum the previous 50 n 
grutenb=list()
x1=list()
x2=list()
x3=list()
x4=list()
x5=list()
for i in range(0,10012):
	temp=trynew.ix[i:i+49:1,4]
	meanmag=temp.sum()/previousn
	grutenb.append(0.434/(meanmag-temp.min())) #0.434 is log e from paper

for x in range(0,len(grutenb)-20):
	x1.append(grutenb[x]-grutenb[x+4])
	x2.append(grutenb[x+4]-grutenb[x+8])
	x3.append(grutenb[x+8]-grutenb[x+12])
	x4.append(grutenb[x+12]-grutenb[x+16])
	x5.append(grutenb[x+16]-grutenb[x+20])
grutenb=pd.DataFrame({'b':grutenb})
x1=pd.DataFrame({'x1':x1})
x2=pd.DataFrame({'x2':x2})
x3=pd.DataFrame({'x3':x3})
x4=pd.DataFrame({'x4':x4})
x5=pd.DataFrame({'x5':x5})
trynew=pd.concat([trynew,grutenb,x1,x2,x3,x4,x5], ignore_index=False, axis=1)

print(trynew)
trynew.to_csv('cleanearthquake.csv',encoding='utf-8')