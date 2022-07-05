import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#reduce 2nd order to 1st order 2 ode's then pass conditions as array

# theta" + (b/m)*theta' + (g/l)*sin(theta) = 0 with inital cond ---> theta' --> velocity at t=0 is 0 and Angle theta = 0
# put theta' = z
# z' + (b/m)*z + + (g/l)*sin(theta) = 0

def model(z,t,b,m,l,g):
    theta = z[0]
    theta1 = z[1]
    theta2 = -(b/m)*theta1 - (g/l)*np.sin(theta)
    resultz = [theta1, theta2]
    return resultz

#inital cond
z0 = [np.pi/6, 0]

#args
b=1
m=1
l=0.5
g=9.8

args = (b,m,l,g,)

#time pts
t = np.linspace(0,10,500)

z = odeint(model,z0,t,args=args)

#seperate theta only from z because z also contains velocity
theta = z[:,0]

plt.plot(t,theta)
plt.show()