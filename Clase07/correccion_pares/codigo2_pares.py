# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:45:49 2021

@author: Rosario Suarez Anzorena
"""

#random_walk.py

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1000)
def randomwalk(largo):
    pasos = np.random.randint (-1,2,largo) 
    return pasos.cumsum()

N = 100000
maximo = 0
minimo = 1000


plt.figure(figsize=(10, 7), dpi=80)
plt.subplot(2, 1, 1)

for i in range(12):
    pasos = randomwalk(N)
    plt.plot(pasos, linewidth= 0.5)
    max_alej = (np.max(abs(pasos))) #Busco el valor absoluto máximo del array
    plt.xticks([])
    plt.ylim(-700, 700)
    #plt.xlabel('tiempo', fontsize = 13)
    plt.ylabel('Distancia al origen', fontsize = 13)
    plt.title('12 Caminatas al azar', fontsize = 13)
    if max_alej >= maximo: 
        print('max',maximo,i)
        maximo = max_alej
        print('max',maximo,i)
        maxi = pasos #Guardo la caminata que más se aleja
    if max_alej < minimo: 
        print('min',minimo,i)
        minimo = max_alej
        print('min',minimo,i)
        mini = pasos #Guardo la caminata que menos se aleja 

    
plt.subplot(2, 2, 3) #grafico de la izquierda
plt.plot(maxi, linewidth= 0.5, color ='Blue')
plt.title('La caminata que más se aleja', fontsize = 13)
plt.ylim(-700, 700)
plt.xticks([])

plt.subplot(2, 2, 4) #gráfico de la derecha
plt.plot(mini, linewidth= 0.5, color ='Blue')
plt.title('La caminata que menos se aleja', fontsize = 13)
plt.ylim(-700, 700)
plt.xticks([])

plt.show()