from __future__ import print_function
import numpy as np
import datetime

def datestr2num(s):
   return datetime.datetime.strptime(s, "%d-%m-%Y").toordinal()

dates,closes=np.loadtxt('AAPL.csv', delimiter=',', usecols=(1, 6), converters={1:datestr2num}, unpack=True)
indices = np.lexsort((dates, closes))

print("Indices", indices)
print(["%s %s" % (datetime.date.fromordinal(int(dates[i])),  closes[i]) for i in indices])
