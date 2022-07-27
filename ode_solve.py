from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math as m

# def model(z,t,b,m,g,l):
#     theta = z[0]
#     theta1 = z[1]
#     theta2 = -(b/m)*theta1 -(g/l)*np.sin(theta)
#     return [theta1, theta2]

def temp(te,t,tin,q,m,cp):
    te = tin - te + q/(m*cp)


# b=0.05
# l=1
# g=9.8
# m=1
# z0=[np.pi/4, 0]
#z0=[0, 1]
t = np.linspace(0,200,500)
# a=(b,l,m,g,)


q = 100000
m = 10
cp = 4.1
tin = 293.15
te0 = 293.15

te = odeint(temp,te0,t,args=(tin,q,m,cp))


# z = odeint(model,z0,t,args=a)

# theta = z[:,0]

#plt.plot(t,theta)
plt.plot(t,te)
plt.show()
