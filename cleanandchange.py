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
trynew.to_csv('cleanearthquake.csv',encoding='utf-8')

'''
print(trynew)
with open("cleanearthquake.csv","w") as f:
	write=csv.writer(f)
'''
	#distance.append(temp[0][-9:-2:])
'''
print(distance)

for x in distance:
	if '方' in x:
		distance2.append(float(x[-3:]))
	if '公' in x:
		pass
	else:
		distance2.append(float(x))

distance=distance2
#print(distance)
'''