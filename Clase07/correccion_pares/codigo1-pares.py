# -*- coding: utf-8 -*-
#random_walk.py

import numpy as np
import matplotlib.pyplot as plt

#EJERCICIO 7.10
np.random.seed(1000)

def menos_lejos(lejos, caminatas):
    menos = lejos.index(min(lejos))
    menos_lejana = caminatas[menos]
    return menos_lejana

def mas_lejos(lejos, caminatas):
    mas = lejos.index(max(lejos))
    mas_lejana = caminatas[mas]
    return mas_lejana

def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo) 
    return pasos.cumsum()    

N = 100000
caminos = 12
caminatas = [randomwalk(N) for i in range(0, caminos)]
lejos = [sum(abs(caminata)) for caminata in caminatas] 

fig = plt.figure(1)
plt.subplot(2, 1, 1)
for caminata in caminatas:
    plt.plot(caminata)
plt.title("12 Caminatas al azar")
plt.xticks([])
plt.yticks([-500, 0, 500])

plt.subplot(2, 2, 3)
plt.plot(mas_lejos(lejos, caminatas))
plt.title("Caminata que más se aleja")
plt.xticks([])
plt.yticks([-500, 0, 500])

plt.subplot(2, 2, 4)
plt.plot(menos_lejos(lejos, caminatas))
plt.title("Caminata que menos se aleja")
plt.xticks([])
plt.yticks([-500, 0, 500])

plt.show()