#random_walk.py
#ejercicio 7.10


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1000)
def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)   
    return pasos.cumsum()

N = 100000
fig = plt.figure()
lista = []
maxs=[]

plt.subplot(2, 1, 1) # define la figura de arriba
for i in range(12):  #las 12 caminatas
    ran=randomwalk(N)
    lista.append(ran)
    maxs.append(max(abs(ran))) #armo lista con el valor absoluto del maximo de cada caminata
    plt.plot(ran)
plt.xticks([])
plt.ylim(-1000,1000)
plt.yticks([-500,0,500] )
plt.ylabel("distancia al origen")
plt.title("12 caminatas al azar", fontsize=8)

#busco a cual de las 12 caminatas corresponde el maximo de los maximos (pues es la que mas se aleja) 
#y el minimo de los maximos (pues es la que menos se aleja)
indice_max=maxs.index(max(maxs))
indice_min=maxs.index(min(maxs))


plt.subplot(2, 2, 3) # define la figura de abajo a la izq
plt.ylim(-1000,1000) 
plt.plot(lista[indice_max])
plt.yticks([-500,0,500])
plt.xticks([])
plt.ylabel("distancia al origen")
plt.title("la caminata que mas se aleja" , fontsize=8)


plt.subplot(2, 2, 4) # define la fig de abajo a la derecha
plt.plot(lista[indice_min])
plt.ylim(-1000,1000) 
plt.xticks([]), plt.yticks([])
plt.title("la caminata que menos se aleja" , fontsize=8)


plt.show()

