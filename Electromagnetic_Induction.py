#expeyes intialization
import eyes17.eyes
p = eyes17.eyes.open()
from pylab import ∗
import time
import numpy as np

v = p.getvoltage
t, v = p.capture1( 'A1' , 3000000, 100)
plot(t,v)
print(t,v)
show()
