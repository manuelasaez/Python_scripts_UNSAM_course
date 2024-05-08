#generala_servida.py
#ejercicio 5.1

import random

def tirar(): 
	'devuelve una lista con cinco dados generados aleatoriamente'
	tirada=[]
	for i in range(5):
		tirada.append(random.randint(1,6)) 

	return tirada

def es_generala(tirada):
	'devuelve True si y sólo si los cinco dados de la lista tirada son iguales'
	generala = False

	if tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada [3] and tirada[3] == tirada[4]:
		generala = True
	return generala



#llamo funcion tirada
#tirada = tirar()
#print(tirada)

#llamo funcion es_generala
#gene = es_generala(tirada)
#print(gene)

#N es la cantidad de tiradas
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')




