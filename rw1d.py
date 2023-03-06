# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:17:44 2022

@author: justo
"""

import matplotlib.pyplot as plt
import numpy as np
from math import *
from random import random
from numpy.random import seed
seed(2)

n = 100   # numero de pasos (propor al tiempo)
M = 2000  # el numero de eventos o caminantes 
p = 0.35 # probabilida de ir hacia la derecha 
xm=0   # 
x2m =0  
prob=np.zeros(2*n,dtype = int)
for j in range(1,M-1):
    x = n
    for i in range(1, n):
        paso = random()
        if paso < p:
            x = x + 1
        else:
            x = x -1 
    #print(j,x)
    xm = xm+x
    x2m = x2m+x**2 
    prob[x]=prob[x]+1

xbar = xm/(float(M))
x2bar = x2m/(float(M))
#var=x2bar-xbar**2
sigma = np.sqrt(x2bar-xbar**2)
print('<x>=',xbar-n)
print('sigma',sigma)
probNormal = prob/float(M)
xt = np.arange(-n,n)


plt.title("RW 1D :$N = " + str(n) + "$ pasos, $M = " +str(M) +"$ caminantes,$p = " +str(p) +"$")
plt.plot(xt,probNormal)
#plt.plot(xf,'bo')
plt.xlabel('x')
plt.ylabel('probabilidad')
plt.legend()


