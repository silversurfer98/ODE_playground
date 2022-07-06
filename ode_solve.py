from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math as m

def model(z,t,b,m,g,l):
    theta = z[0]
    theta1 = z[1]
    theta2 = -(b/m)*theta1 -(g/l)*np.sin(theta)
    return [theta1, theta2]


b=0.05
l=1
g=9.8
m=1
z0=[np.pi/4, 0]
#z0=[0, 1]
t = np.linspace(0,200,500)
a=(b,l,m,g,)

z = odeint(model,z0,t,args=a)

theta = z[:,0]

plt.plot(t,theta)
plt.show()
