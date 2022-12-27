import numpy as np
import matplotlib.pyplot as plt
import eyes17.eyes
import time
import scipy.fftpack as fft

p = eyes17.eyes.open()

x = np.zeros(10001)
t = np.zeros(10001)
timp = np.zeros(10)
start = time.time()

for i in range(10):
    start = time.time()
    a = 0
    tim = 0
    while (tim<=2):
        t[a],x[a]=p.sr04_distance_time()
        t[a] = t[a] - start
        tim = time.time() - start
        a = a+1
        
    x1 = np.zeros(a)
    t1 = np.zeros(a)
    for j in range(a):
        x1[j] = x[j]
        t1[j] = t[j]
    tp = fft.fftfreq(x1.size, d = (t1[-1]/len(t1)))   # one side frequency range
    Y = fft.fft(x1)
    maxi = np.max(abs(Y))
    for j in range(len(Y)):
        if abs(Y[j]) == maxi:
            Y = np.delete(Y,j)
            tp = np.delete(tp,j)
            break
            
    maxi = np.max(abs(Y))
    for j in range(len(Y)):
        if abs(Y[j]) == maxi:
            timp[i] = tp[j]
            break
            
    print(timp[i])
