import matplotlib.pyplot as plt
import eyes17.eyes
import numpy as np
from scipy import stats
p = eyes17.eyes.open()

print("Enter 1 if you know the Spring Constant \n Enter 2 if you don't know the value of spring constant")
n = int(input())
d0 = p.sr04_distance()
if n==1:
    m1 = 0
    m = np.zeros(8)
    x = np.zeros(8)
    for i in range(8):
        m[i] = float(input('Enter the value of mass added in KG'))
        m1 = m1 + m[i]
        m[i] = m1 * 9.81
        x[i] = d0 - (p.sr04_distance())
        
    slope, intercept, corr, s, err = stats.linregress(m,x)
    print(1/slope,corr)
    Spring_Constant = 1/slope
    print('Place weight on weighing machine and press 1')
    c = int(input())
    if c==1:
        dx = p.sr04_distance()
        wt = Spring_Constant*((d0-dx)/9.81)
        print('weight is',wt,'K.G.')
        
if n==2:
    Spring_Constant = float(input('Enter spring constant'))
    print('Place weight on weighing machine and press 1')
    c = int(input())
    if c==1:
        dx = p.sr04_distance()
        wt = Spring_Constant*((d0-dx)/9.81)
        print('weight is',wt,'K.G.')
