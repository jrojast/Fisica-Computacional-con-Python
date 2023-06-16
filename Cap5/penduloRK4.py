# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 21:15:16 2021
pendulo
@author: justo
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi
#=============================================================
def acel(t,ang,w):
    """
    acel: funcion de aceleracion angular
    t: vector tiempo
    ang: angulo en radianes
    w: velocidad angular
    Coeficientes:
        Q - relacionado con el coeficiente de friccion
        F - frecuencia natural sqrt(L/g)
        Omega - frecuencia de la fuerza externa
        B - amplitud de la fuerza externa A/ml
    """    
    return -Q*w-F*np.sin(ang)+B*np.cos(Omega*t)
#=============================================================
def RK4(acel,teta0,v0,h,t):
  """
  Algoritmo de Runge-Kutta de 4to orden
  acel: funcion aceleracion
  t: vector con los puntos discretos de la variable independiente
  y0, v0 : valor inicial de la funcion y  y v
  h : paso de tiempo
  """
  n = len(t)
  ang = np.zeros(n)  # funcion que se busca y(t) 
  w = np.zeros(n)   # velocidad abgular
  ang[0] =teta0   
  w[0] = w0
  for i in range(0,n-1):
      k1a = h*w[i]
      k1w = h*acel(t[i],ang[i],w[i])
      k2a = h*(w[i]+k1a/2)
      k2w = h*acel(t[i]+0.5*h,ang[i]+k1a/2,w[i]+k1w/2)
      k3a = h*(w[i]+k2a/2)
      k3w = h*acel(t[i]+0.5*h,ang[i]+k2a/2,w[i]+k2w/2)
      k4a = h*(w[i]+k3a)
      k4w = h*acel(t[i]+h,ang[i]+k3a,w[i]+k3w)
      ang[i+1] = ang[i]+ (k1a+2*k2a+2*k3a+k4a)/6
      w[i+1] = w[i]+ (k1w+2*k2w+2*k3w+k4w)/6
  
  return (ang,w)   # devuelve el vector y

# ========================================================
# condiciones iniciales
h = 0.01     # paso de tiempo
w0 = 1.0
teta0 = 60.0
s = 50
teta0 = teta0*pi/180    # conversion a radianes
t = np.arange(0,s*pi,h)

F = 0.2
Q = 0.1
B = 0. 
Omega = pi/5
#========================================================
print('Solucion numerica')
an , wn = RK4(acel,teta0,w0,h,t)

plt.plot(t,an,'g-',label ='Q0.1, F=1,B=1')
plt.ylabel('angulo')
#plt.plot(,an,'g-',label ='Q0.1')
plt.grid()
plt.legend(loc='upper right')
plt.show()