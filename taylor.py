#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:13:16 2023

@author: justo rojas
Programa que aproxima la funcion f(x) = sin(x) mediante el desarrollo en 
serie de Taylor de diferentes ordenes.

"""

from math import pi, sin ,cos
import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
  f = 1
  for i in range(2,n+1):
    f = f*i
  return f

def T_n(n,x):
    """
    Polinomio de aproximacion de grado n

    Parametros
    ----------
    n : entero
        Grado del polinomio.
    x : real
        punto de aproximacion.

    Devuelve
    -------
    s : real
        Suma parcial.

    """
    s = 0
    for i in range(n):
      s = s+ ((-1)**(i))*x**(1+2*i)/factorial(1+2*i)
    return s


m = 50 # cantidad de puntos
x = np.linspace(-np.pi,np.pi,m)
t1 = []
t3 = []
t5 = []
tex = []
for k in range(len(x)):
  sin_aprox = 0
  sm1 = T_n(1,x[k])
  t1.append(sm1)
  sm3 = T_n(3,x[k])
  t3.append(sm3)
  sm5 = T_n(5,x[k])
  t5.append(sm5)
  se = sin(x[k]) 
  tex.append(se)

# Representacion grafica de los datos
plt.plot(x,t1,label='orden 1')
plt.plot(x,t3,label='orden 3')
plt.plot(x,t5,label='orden 5')
plt.plot(x,tex,label='sin(x)')
plt.xlabel('x,radianes')
plt.ylabel('sin(x)')
plt.grid()
plt.legend()
plt.title('Aproximacion de sin(x) ')




