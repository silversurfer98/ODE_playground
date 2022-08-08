import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define a function which will return dy/dt

def model(y,t,arg1,arg2):
    dydt = y*arg1 + arg2
    return dydt

# define intial condition
y0 = 0.1

# define arguments
a = 2
b = 0
# always group them in tuples
arguments = (a,b,)

#define time points  --> here 50 means 50 pts inbetween 0 and 20
t = np.linspace(0,10,1000)

# now we ready to solve
y = odeint(model,y0,t,args=arguments)

#now graph it
plt.plot(t,y)
#plt.yscale('log')
plt.show()
