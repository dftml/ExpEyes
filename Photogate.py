import time
import numpy as np
import eyes17.eyes
import time
p = eyes17.eyes.open()

print('\tWelcome')
print('Enter your choice')
print('1. Stopwatch \n2. Velocity \n3. Acceleration \n4. g by freefall \n5. Time Period')
choice = int(input())

def stopwatch():
    print('\tStopwatch')
    print('Enter your Choice')
    print('1.Start \n2. Exit')
    ch = int(input())
    if ch==1:
        start = time.time()
        print('Enter 1 for lap and anything else to Stop')
        n = int(input())
        l = 1
        while n==1:
            if n==1:
                lap[1] = time.time() - start
                l = l+1
                
            n = int(input())
        stop = time.time()-start
        print('Time elapsed is', stop)
        print('laps are')
        for i in range(l):
            print(i,lap[i])
            
            
def velocity():
    x = float(input('Enter distance between pickets or photogates'))
    n = 1
    while n==1:
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b)<5000:
            b = p.get_resistance()
            
        start1 = time.time()
        
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b)<5000:
            b = p.get_resistance()
        end1 = time.time()
        v = x/(end1-start1)
        print('Velocity is', v,'m/sec')
        print('Press 1 to continue or any other key to quit')
        n = int(input())
        
        
def acceleration():
    x = float(input('Enter distance between pickets or photogates'))
    n = 1
    while n==1:
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b)<5000:
            b = p.get_resistance()
        start1 = time.time()
        start = time.time()
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b) < 5000:
            b = p.get_resistance()
        end1 = time.time()
        v = x/(end1-start1)
        
        print('Velocity is',v,'m/sec')
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b)<5000:
            b = p.get_resistance()
        start1 = time.time()
        
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b) < 5000:
            b = p.get_resistance()
        end1 = time.time()
        end = time.time()
        v2 = x/(end1-start1)
        print('Velocity is', v2, 'm/sec')
        a = (v2-v) / (end-start)
        print('Acceleration is', a, 'm/(sec*sec)')
        print('Press 1 to continue or any other key to quit')
        n = int(input())
        
        
def g_freefall():
    x = float(input('Enter distance between pickets or photogates'))
    s = float(input('Enter distance between point of drop and photogate'))
    n = 1
    while n==1:
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b)<5000:
            b = p.get_resistance()
        start1 = time.time()
        
        a = p.get_resistance()
        b = p.get_resistance()
        while abs(a-b) < 5000:
            b = p.get_resistance()
        end1 = time.time()
        v = x/(end1-start1)
        print('Velocity is',v,'m/sec')
        g = (v*v)/(2*s)
        print('Acceleration due to gravity is',a,'m/(sec*sec)')
        print('Press 1 to continue or any other key to quit')
        n = int(input())
        
def time_period():
    start = time.time()
    a = np.zeros(100000)
    t = np.zeros(100)
    i = 1
    j = 0
    a[0] = p.get_resistance()
    while i <= 10000:
        a[i] = p.get_resistance()
        if a[i] - a[i-1] > 150:
            t[j] = time.time() - start
            print('time when pendulum in mid position', t[j])
            j = j+1
            
        i = i+1
    n = len(t)
    sum_=0
    for i in range(n-1):
        sum_= sum_+t[j+1]-t[j]
    sum_ = sum_/n
    print('Average time of half oscillation = ', sum_)
    print('program execution time =', time.time()-start)
    
        
        
if choice==1:
    stopwatch()
    
elif choice==2:
    velocity()
    
elif choice==3:
    acceleration()
    
elif choice==4:
    g_freefall()
    
elif choice==5:
    time_period()
    
else:
    print('Invalid Choice')
