import sys
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import csv

average=list()
minmax=list()
for x in range(1,len(sys.argv)):
	data=pd.read_table(sys.argv[x],encoding='utf8')
	a=data.values
	hourcount=0
	count_num=0
	suma=0
	minnum=100000
	maxnum=-100000
	for x in a:
		temp=x[0].split(" ")
		if float(temp[6])>=maxnum:
			maxnum=float(temp[6])
		if float(temp[6])<=minnum:
			minnum=float(temp[6])
		count_num=count_num+1
		suma=float(suma)+float(temp[6])
	minmax.append([temp[1]+"-"+temp[2]+"-"+temp[3],minnum,maxnum,maxnum-minnum])
	average.append([temp[1]+"-"+temp[2]+"-"+temp[3],suma/count_num])
#print(average)
'''
for x in minmax:
	temp=x[0].split("-")
'''
with open("minmaxhour.csv","w") as f:
	writer=csv.writer(f)
	for x in minmax:
		writer.writerow(x)

with open("averagehour.csv","w") as a:
	writer=csv.writer(a)
	for x in average:
		writer.writerow(x)
rangex=list()
for x in minmax:
	rangex.append(x[3])
plt.plot(rangex)
plt.show()
diff=list() 
temp=0
for x in average:
	diff.append(x[1]-temp)
	temp=x[1]
plt.plot(diff)
plt.ylim(-5,5)
#plt.show()
#python3 fluctuation.py six/201701*.LIU  six/201702*.LIU six/201703*.LIU six/201704*.LIU  six/201705*.LIU six/201706*.LIU six/201707*.LIU  six/201708*.LIU six/201709*.LIU six/201710*.LIU