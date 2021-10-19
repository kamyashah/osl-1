import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt

f = open("statistics.txt",'r')
for line in f:
    a=line.split(',')
    print(a)
x=[]
for i in abc:
    x.append(int(i))
        
print(x)
total=0
        
for i in x:
    total=total+i
            
print("Total: " + str(total))
mean=total / len(x)
print("Mean: " + str(mean))

n = len(x)
x.sort()
  
if n % 2 == 0:
    median1 = x[n//2]
    median2 = x[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = x[n//2]
print("Median: " + str(median))

data = Counter(x)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode: " + ', '.join(map(str, mode))
      
print(get_mode)
sum= 0
for i in x :
     sum +=(i-mean)**2
     stdeV = sqrt(sum/(len(x)-1)) 
print("Standard Deviation: " +str(stdeV))

var=(stdeV)**2
print("Variance: " +str(var))

range= max(x)-min(x)
print("Range: " +str(range))

