#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:30:03 2023

@author: justorojas

"""
# errores  de calculo durante la suma de numeros reales

potencias = [1,2,3,4,5,6,7]
x =1.0
n = 10
print('=================================')
for i in potencias:
    sumai =0.0
    ni = n**i  # numero de veces a sumar
    xi = x/ni  # numero real a sumar
    for k in range(ni):
        sumai = sumai + xi
    error = abs(sumai-1.0) 
    print('sumas con x = ',xi, ni,sumai,error)
    
