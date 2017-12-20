import sys
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


arr=list()
arr2=list()
xl=list()
dates=list()
countls=list()
count=0
starttime=0
finishtime=12
for x in range(1,len(sys.argv)):
	data=pd.read_table(sys.argv[x],encoding='utf8')
	a=data.values
	for x in a:
		temp=x[0].split(" ")
		date=temp[1]+"-"+temp[2]
		if (int(temp[3])>=starttime and int(temp[3])<finishtime):
			count=count+1
			if(count%1000==0):
				countls.append(count)
				xl.append(temp[3]+"-"+temp[4])
			arr.append(temp[-2])

'''
for x in arr:
	print(x[0])
	a=x[0].split(" ")
	arr2.append(a[-2])
'''
#dates = ['01/02/1991', '01/03/1991', '01/04/1991']
plt.xticks(countls,xl,fontsize=7)
plt.plot(arr)
plt.savefig(date+".png")
plt.show()


