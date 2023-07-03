# -*- coding: utf-8 -*-
"""
Calcula la integral de la funcion f(x) mediante el metodo
Monte Carlo plano
@author: justo
"""
import numpy as np

def mcp(a,b,N):
    """
    Parameters
    ----------
    xi : conjunto de N numeros aleatorios uniformemente distribuidos
    en el intervalo a,b  
    fi: vector con los valores de la funcion f(xi)
    sigma : desviacion standart

    Returns
    -------
    integ, sigma 
    """
    xi = np.random.uniform(a,b,N)
    fi = f(xi)
    mean = np.sum(fi)/N
    suma2 = np.sum(fi**2)/N
    integ = mean*(b-a)
    sigma = np.sqrt(suma2-mean**2)
    return integ , sigma 
    
# limites de integracion y la funcion a integrar
f = lambda x: 4*x**3
a , b =0,2
valor_exacto = 16.0
N = 1000000
integral, sigma = mcp(a,b,N)
error = abs(integral- valor_exacto)
print('===============')
print('integral_MC = ','{:6.3f}'.format(integral))
print('sigma = ','{:6.3f}'.format(sigma))
print('error = ','{:6.3f}'.format(error))     
