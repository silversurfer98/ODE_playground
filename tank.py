from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def tank(h,t,fi,p,g,r,a):
    dhdt = (1/a)*(fi - (p*g*h/r))
    return dhdt



fi = 2
a = 10.0
p = 1.0
g = 1.0

#initial cond
#h0 = 0.1

t = np.linspace(0,120,400)
h = np.zeros(len(t))

h0 = 0

r = np.ones(len(t))*0.1

sp = np.ones(len(t))*0.1
sp[100:] = 1
sp[300:] = 1.5
error = np.zeros(len(t))

kc = 2.1
taui = 250.0
taud = 5
sum = 0
lasterror = 0

for i in range(len(t)-1):
    error[i] = sp[i] - h[i]
    sum = sum + (kc/taui)*error[i]
    d = kc/taud * (error[i] - lasterror)
    r[i] = r[0] + kc*error[i] + sum + d
    temp = odeint(tank,h0,[t[i],t[i+1]],args=(fi,p,g,r[i],a,))
    #print(temp)
    h0 = temp[1]
    h[i+1] = temp[1]
    lasterror = error[i]

plt.plot(t,h)
plt.plot(t,sp,'r--')
plt.show()