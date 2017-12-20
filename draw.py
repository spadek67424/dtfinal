import sys
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import csv
minmax=list()
average=list()
with open("minmaxhour.csv","r") as f:
	readerx=csv.reader(f)
	for x in readerx:
		minmax.append(x)

with open("averagehour.csv","r") as a:
	readery=csv.reader(a)
	for x in readery:
		average.append(x)

rangex=list()
for x in minmax:
	rangex.append(x[3])
plt.plot(rangex)
plt.ylim(0,10)
plt.show()

diff=list() 
temp=0
for x in average:
	diff.append(x[1]-temp)
	temp=x[1]
plt.plot(diff)
plt.ylim(-5,5)