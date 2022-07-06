from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def tank(h,t,fi,p,g,r,a):
    dhdt = (1/a)*(fi - (p*g*h/r))
    return dhdt



fi = 1.1
r = 0.09
a = 10.0
p = 1.0
g = 1.0

#initial cond
h0 = 0.5

t = np.linspace(0,30,100)

h = odeint(tank,h0,t,args=(fi,p,g,r,a,))

plt.plot(t,h)
plt.show()