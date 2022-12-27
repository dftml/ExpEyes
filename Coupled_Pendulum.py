import eyes17.eyes
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
p = eyes17.eyes.open()

l = input("Number of data points : ")

T = np.zeros(l)
D = np.zeros(l)

start = time.time()

i = 0

while (i<1):
    T[i], D[i] = p.sr04_distance_time()
    T[i] = T[i] - start
    print(T[i], D[i])
    i = i + 1
    
    
ss = abs(T[-1]-T[-2])
frq = np.fft.fftfreq(D.size, d=ss)

y = np.fft.fft(D)
y_sort = y.sort()

fig, ax = plt.subplots(2,1)
ax[0].plot(T,D)
ax[1].plot(abs(frq), abs(y))
plt.show()
