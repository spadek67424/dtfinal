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

a=trynew.loc[trynew['magnitude']>5]
b=trynew['magnitude']>6
for x in range(0,9):
	temp=trynew['magnitude']>x
	temp2=temp.value_counts(sort=False)
	
	