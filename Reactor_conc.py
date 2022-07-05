import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# http://apmonitor.com/pdc/index.php/Main/TankBlending

# model is
# ReactorV * Ca'  + Ca_in * Vin = Ca_out * Vout
# Vin = Vout = q

def reactor(ca,t,V,q,caf):
    dCadt = (q/V)*(caf - ca)
    return dCadt

Ca0 = 0
q = 100
V = 100
caf = 1

t = np.linspace(0,10,100)

ca = odeint(reactor,Ca0,t,args=(V,q,caf,))

plt.plot(t,ca)
plt.show()