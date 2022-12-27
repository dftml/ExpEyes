import matplotlib.pyplot as plt
import numpy as np
import eyes17.eyes
from scipy import stats
p = eyes17.eyes.open()

v = np.zeros(200)
r = np.zeros(200)
I = np.zeros(200)
I[0] = 100
r[0] = p.get_resistance()
v[0] = p.get_voltage('A2')

for i in range(1,200):
    v[i] = p.get_voltage('A2')
    r[i] = p.get_resistance()
    I[i] = I[i-1]*pow((r[i-1]/r[i]), 0.6)
    
    
# code for least square fit

m, c, corr, s, err = stats.linregress(r,v)
r1 = np.linspace(r[0],r[199])
v1 = m*r1 + c

fig, ax  = plt.subplots(1,3)
s = 'Voltage vs Resistance'
ax[0].set_title(s)
ax[0].plot(r,v,'-',r1,v1,'--')
ax[0].set_xlabel('Resistance (Ohm)')
ax[0].set_ylabel('Voltage (V)')
ax[0].grid()
s = 'Voltage vs Intensity'
ax[1].set_title(s)
ax[1].plot(I,v,'-')
ax[1].set_xlabel('Relative Intensity')
ax[1].set_ylabel('Voltage (V)')
ax[1].grid()
s = 'Resistance vs Intensity'
ax[2].set_title(s)
ax[2].plot(I,r,'-')
ax[2].set_xlabel('Relative Intensity')
ax[2].set_ylabel('Resistance (Ohm)')
ax[2].grid()
plt.show()
