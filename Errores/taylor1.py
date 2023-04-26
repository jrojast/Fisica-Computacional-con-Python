"""
Programa que aproxima la funcion f(x) = cos(x) mediante el desarrollo en 
serie de Taylor de diferentes ordenes.
"""

from math import pi , sin
import numpy as np
import matplotlib.pyplot as plt
def factorial(n):
    """
        Parameters
    ----------
    n : integer
        DESCRIPTION.

    Returns
    -------
    factor : integer
        factorial de N.

    """
    factor =1
    for i in range(1,n+1):
        factor = factor*i
    return factor

nm = [0,1,2,3,4,5,6,7]


inx = np.linspace(-2*pi,2*pi,51)
p = len(inx)
f = np.zeros((p,10))
f[:,0] =inx 


for j in range(p):
    x = inx[j]
    su =0.
    for k in nm:
        su = su +(-1)**k*x**(2*k)/factorial(2*k)
        f[j,k]=su
        

it = np.cos(inx)
plt.title('Aproximacion del cos(x)')
plt.plot(inx,it, color ='red',linewidth =2.0,label ='exacto')
plt.plot(inx,f[:,1],label ='n=1')
plt.plot(inx,f[:,3],label ='n=3')
plt.plot(inx,f[:,5],label ='n=5')
plt.plot(inx,f[:,7],label ='n=7')
plt.ylim(-3,1.5)
plt.legend()
plt.grid()


      


    
