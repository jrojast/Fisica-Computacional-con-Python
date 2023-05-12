"""
Programa que implementa el movimiento de los Planetas
al rededor del sol mediante la solucion numerica de las 
ecuaciones diferenciales de movimiento.
En unidades astronomicas
"""
from math import *
import numpy as np
import matplotlib.pylab as plt
def planetas(tmax,x0,vy0):
    GM = 4*pi**2      # 
    pos = np.array([1.0,0.0])
    vel = np.array([0.0,vy0])
    acel = np.array([0.0,0.0])
    xl = []
    yl = []
    tl = []
    t = 0.0
    dt = 0.002   # aprox 10 dias
 
    while t <= tmax:
        r = sqrt(pos[0]**2+pos[1]**2)
        for i in range(2):
 #        print('{:4.2f}{:12.4f}{:12.4f}{:12.4f}{:12.4f}'.format(t,pos[0],pos[1],vel[0],vel[1]))
            acelt=-GM*pos[i]/r**3
            pos[i] = pos[i]+vel[i]*dt  + 0.5*acelt*dt*dt        
            acel[i]=-GM*pos[i]/r**3
            vel[i] =vel[i]+dt*(acel[i]+acelt)*0.5
            tl.append(t) 
            xl.append(pos[0])
            yl.append(pos[1])
            t = t +dt
    return (tl,xl,yl)

vy0 = 5.2
tmax = 6.0
tt,xx,yy = planetas(tmax,1.,vy0)

plt.title('orbita de la tierra con v0=5.2 u.a')
plt.plot(xx,yy,'b-')
plt.ylabel('y',fontsize=14)
plt.xlabel('x',fontsize=14)
plt.grid()
plt.axis('equal')
plt.plot(0.,0.,'ro')
plt.figure(2)
plt.plot(tt,xx)
plt.xlabel('t')
plt.ylabel('y')
