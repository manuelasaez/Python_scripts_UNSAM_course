#figuritas.py
#Ejercicio 5.3
'''
import numpy as np
import random


 #0 para indicar que aún no la conseguimos y 1 para indicar que sí 
n = 670 #cantidad total de figus
album = np.zeros(n) #armo vector de 670 ceros

contador = 0
while 0 in album: 
	num_de_figu = random.randint(1,670)
	if album[num_de_figu-1] >= 1:
		album[num_de_figu-1]+=1
	else:
		album[num_de_figu-1]=1
	contador+=1
print(f'La cantidad de figuritas que tuve que comprar para llenar el album es de {contador}')
print(f'El album quedo rellenado de la siguiente manera {album}')

'''


#ejercicio 5.9-5.10.511 y 5.12
import numpy as np
import random


def crear_album(figus_total):
	'crea un album vacio de figuritas'
	album = np.zeros(figus_total) #armo vector de 670 ceros.
	return album

def album_incompleto(A):
	'recibe un vector y devuelve True si el vector contiene el elemento 0, y False en otro caso.'
	#VERSION USANDO PROD()
#	var = True
#	if (A != 0).prod(): # np.prod hace el producto de los elementos de A, si algun elemento es cero, da cero.
#	if (A != 0).prod():  #if o in A:
#		var = False
#	return var
#VERSION USANDO IN
	var = False
#	if (A != 0).prod(): # np.prod hace el producto de los elementos de A, si algun elemento es cero, da cero.
	if 0 in A:
		var = True
	return var

def	comprar_figu(figus_total):
	'recibe número total de figuritas que tiene el álbum y devuelve un número entero aleatorio'
	num_de_figu = random.randint(1,figus_total)
	return num_de_figu


def cuantas_figus(figus_total):
	'genera un album nuevo, simula su llenado y devuelve la cantidad de figuritas que se debieron comprar para completarlo'

	album = crear_album(figus_total) 	#genero album nuevo
	contador = 0 #inicializo contador
	while album_incompleto(album): 
		num_de_figu = comprar_figu(figus_total)  #calculo num de figu random
		if album[num_de_figu-1] >= 1:  #resto uno en el indice proque las figus estan entre 1 y 670, pero el indice de album 0 a 669.
			album[num_de_figu-1] += 1
		else:
			album[num_de_figu-1] = 1
		contador+=1
	return contador, album


n = 670 #cantidad total de figus
contador, album = cuantas_figus(n)

print(f'La cantidad de figuritas que tuve que comprar para llenar el album de {n} figuritas es de {contador}')
#print(f'El album quedo rellenado de la siguiente manera {album}')


#ejercicio 5.13
n_repeticiones = 1000
figus_total = 6 
lista = [cuantas_figus(figus_total)[0] for i in range(n_repeticiones)]
prom = np.mean(lista)

print(f'En promedio, hay que comprar {prom} figuritas, para completar el álbum de {figus_total} figuritas')

#ejercicio 5.14
n_repeticiones = 100
figus_total = 670 
lista = [cuantas_figus(figus_total)[0] for i in range(n_repeticiones)]
prom = np.mean(lista)
print(f'En promedio, hay que comprar {prom} figuritas, para completar el álbum de {figus_total} figuritas')