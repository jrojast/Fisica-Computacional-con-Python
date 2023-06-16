#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:32:33 2023

@author: justorojas
"""
"""
# generacion de N numeros aleatorios enteros mediante el algoritmo de congruencia
# lineal

N = 50
a, c,m = 3,5,60
x = 6
vx = []
vr =[]
for i in range(50):
    x = (a*x+c) % m # numero entero
    r = x/m
    vx.append(x)
    vr.append(r)
    
print(vx)
print(vr)
import matplotlib.pyplot as plt
plt.hist(vr)
 """
# Pregunta 2. Generar un vector x con N =20 componentes
# reales, cuyos valores esten entre 2 y 12

import numpy as np
# para obtener en intervalo a,b
# a +(b-a)*na
"""
a,b = 2,12
N = 2000
x = a+(b-a)*np.random.rand(N)
import matplotlib.pyplot as plt
plt.hist(x)
plt.xlabel('x')
"""
# Pregunta 2.e generar N puntos en los limites de un 
# cuadrado de lado l = 10
import matplotlib.pyplot as plt
N = 2000
l = 10 
x = l*np.random.rand(N)
y = l*np.random.rand(N)
plt.plot(x,y,'bo')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')


