#ejercicio 4.6 y 4.7
#busqueda_en_listas.py
 
def buscar_u_elemento(lista,e):
	'''Si e está en la lista devuelve la posición de la ultima vez que aparece, de lo
    contrario devuelve -1.
    '''
	pos = -1  # comenzamos suponiendo que e no está
	for i, z in enumerate(lista): # recorremos la lista
		if z == e:   # si encontramos a e
			pos = i  # guardamos su posición, saque el break, para que vuelva a entrar en caso de que el elemento este mas adelante.
	return pos


def buscar_n_elemento(lista,e):
	'''recibe una lista y un elemento y devuelve la cantidad de veces que aparece el elemento en la lista'''
	cant=0
	for i in lista:
		if i == e:
			cant+=1
	return cant
'''
#maximo sin cambiar inicializacion de m:
def maximo(lista):
	'Devuelve el máximo de una lista, la lista debe ser no vacía y de números positivos.'

	m = 0
	for e in lista: # Recorro la lista y voy guardando el mayor
		if e > 0 and e > m:
			m = e
		elif e < 0 and abs(e) < abs(m):  #si es negativo comparo su valor absoluto y me quedo con el mas cercano al 0 (pues es mas grande)
			m = e
	return m
'''

#maximo cambiando inicializacion de m por el primer elemento de la lista:
def maximo(lista):
	'''Devuelve el máximo de una lista, 
	la lista debe ser no vacía y de números positivos.
	'''
	m = lista[0]
	for e in lista: # Recorro la lista y voy guardando el mayor
		if e > m:
			m = e
	return m

def minimo(lista):
	'''Devuelve el máximo de una lista, 
	la lista debe ser no vacía y de números positivos.
	'''
	m = lista[0]
	for e in lista: # Recorro la lista y voy guardando el mayor
		if e < m:
			m = e
	return m

lista = [-1,-2,-3,-2,-3,-4]
e=-2

posicion=buscar_u_elemento(lista,e)
print(f'La posicion donde se encuentra el elemento {e} por ultima vez es: {posicion} (recordar que si arroja -1 es que no esta)')

contador=buscar_n_elemento(lista,e)
print(f'La cantidad de veces que aparece el elemento {e} es: {contador}')

maxi= maximo(lista)
print(f'El maximo de la lista es: {maxi}')

mini=minimo(lista)
print(f'El minimo de la lista es: {mini}')
