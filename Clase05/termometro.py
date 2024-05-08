#termometro.py
#ejercicio 5.5
'''
import random

mu = 0
sigma= 0.2
temp=37.5
temperaturas = []
for i in range(99):
	temperaturas.append(random.normalvariate(mu+temp,sigma))
print(temperaturas)


maximo = max(temperaturas)
minimo = min(temperaturas)
promedio = sum(temperaturas)/len(temperaturas)
temp_orden = sorted(temperaturas)
mediana = temp_orden[len(temperaturas)//2]
print(f'El maximo es {maximo}')
print(f'El minimo es {minimo}')
print(f'El promedio es {promedio}')
print(f'La mediana es {mediana}')
'''

###############
#Ejercicio 5.7
#transformo salida a numpy array y guardo en archivo en carpeta DATA


import numpy as np
import random

mu = 0
sigma= 0.2
temp=37.5
temperaturas = []
for i in range(999):
	temperaturas.append(random.normalvariate(mu+temp,sigma))

#lo trasnformo a numpy array 
temperaturas_array = np.array(temperaturas)
np.save('../Data/Temperaturas.npy', temperaturas_array)
#si lo quiero hacer con numpy arrays
#maximo = temperaturas_array.max()
#minimo = temperaturas_array.min()
#promedio = temperaturas_array.sum()/temperaturas.size

#si lo hago con lista
maximo = max(temperaturas)
minimo = min(temperaturas)
promedio = sum(temperaturas)/len(temperaturas)
temp_orden = sorted(temperaturas)
mediana = temp_orden[len(temperaturas)//2]


print(f'El maximo es {maximo}')
print(f'El minimo es {minimo}')
print(f'El promedio es {promedio}')
print(f'La mediana es {mediana}')
