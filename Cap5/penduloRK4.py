# -*- coding: utf-8 -*-
"""
Programa que implementa la solucion numerica mediante el algoritmo
de Runge-Kutta de 4to orden de las ecuaciones diferenciales que 
gobiernan el comportamiento del pendulo matematico

@author: justo
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos 
#=============================================================
def acel(t,w,ang):
    """
    acel: funcion de aceleracion angular
    t: vector tiempo
    ang: angulo en radianes
    w: velocidad angular
    Coeficientes:
        Q - relacionado con el coeficiente de friccion
        Fn - frecuencia natural sqrt(L/g)
        Omega - frecuencia de la fuerza externa
        B - amplitud de la fuerza externa A/ml
    """    
    return -Q*w-Fn**2*sin(ang)+B*cos(Omega*t)

def f1(t,w,ang):
    return w

#=============================================================
def RK4(teta0,v0,h,t):
  """
  Algoritmo de Runge-Kutta de 4to orden
  acel: funcion aceleracion
  t: vector con los puntos discretos de la variable independiente
  teta0, w0 : valor inicial del angulo y velocidad
  h : paso de tiempo
  """
  n = len(t)
  ang = np.zeros(n)  # funcion que se busca ang(t) 
  w = np.zeros(n)   # velocidad abgular
  ang[0] =teta0   
  w[0] = w0
  for i in range(0,n-1):
      k1a = h*f1(t[i],w[i],ang[i])
      k1w = h*acel(t[i],w[i],ang[i])
      k2a = h*f1(t[i]+h/2,w[i]+k1w/2,ang[i]+k1a/2)
      k2w = h*acel(t[i]+0.5*h,w[i]+k1w/2,ang[i]+k1a/2)
      k3a = h*f1(t[i]+h/2,w[i]+k2w/2,ang[i]+k2a/2)
      k3w = h*acel(t[i]+0.5*h,w[i]+k2w/2,ang[i]+k2a/2)
      k4a = h*f1(t[i]+h,w[i]+k3w,ang[i]+k3a)
      k4w = h*acel(t[i]+h,w[i]+k3w,ang[i]+k3a)
      ang[i+1] = ang[i]+ (k1a+2*k2a+2*k3a+k4a)/6
      w[i+1] = w[i]+ (k1w+2*k2w+2*k3w+k4w)/6
  
  return (ang,w)   

# ========================================================
# condiciones iniciales
h = 0.1     # paso de tiempo
w0 = 0.0
teta0 = 30.0
Fn = 1.5
Q = 0.05
B = 0.5
Omega = 1.45
s = 40
teta0 = teta0*pi/180    # conversion a radianes
t = np.arange(0,s*pi,h)
an , wn = RK4(teta0,w0,h,t)
#========================================================
plt.figure(1)
plt.title("Pendulo con : $Q = " + str(Q) + "$, $B ="+str(B)+"$")
plt.plot(t,an,'g-')
plt.ylabel('Angulo (rad)')
plt.xlabel('t(s)')
plt.grid()
plt.legend(loc='upper right')
plt.show()
plt.figure(2)
plt.title("Pendulo con : $Q = " + str(Q) + "$, $B ="+str(B)+"$")
plt.plot(an,wn)
plt.ylabel('Angulo')
plt.xlabel('velocidad')
plt.grid()
