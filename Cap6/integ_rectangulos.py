# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:24:24 2022

@author: justo rojas

Programa que calcula numericamente la integral definida de la funcion f(x) 
mediante el metodo de los rectangulos. 

"""

import numpy as np

def integ_rectangulo (N,a,b,f):
    """
    a,b: limites de integracion
    N: cantidad de subintervalos
    f: funcion a integrar
    """
    dx = (b-a)/N
    x = np.arange(a,b,dx)
    suma = 0
    for i in range(N):
        suma = suma + f(x[i])
        
    integral = dx*suma
    return integral
        
# funcion a integrar 
f = lambda x: 4*x**3
a,b = 0.0,2

#  En caso cuando se conoce la solucion exacta, el siguiente codigo muestra 
#  la dependencia del error de calculo del numero N
valor_exacto = 16.0
m = [10**k for k in range(1,7)]
print('       N    integral     error')
for j in m:
    integral_N = integ_rectangulo(j,a,b,f)
    error = abs(integral_N - valor_exacto)
    print('{:8d}{:12.6f}{:12.6f}'.format(j,integral_N,error))
    
