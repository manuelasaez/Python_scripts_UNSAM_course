#arboles.py
##############################################################

#ejercicio 3.18

##############################################################
'''
import csv
def leer_parque(nombre_archivo, parque):
	'abre el archivo indicado y devuelve una lista de diccionarios con la información del parque especificado'
	with open(nombre_archivo, 'rt') as f:
		lista_parque = []
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record=dict(zip(headers, row))  #armo dicc con dict(zip)
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				if record['espacio_ve'] == parque:
					lista_parque.append(record)  #appendea los dicc a la lista camion
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return lista_parque

parque='GENERAL PAZ'
lista_de_parque=leer_parque('../Data/arbolado-en-espacios-verdes.csv',parque)
#print(len(lista_de_parque)) #chequeo que sean 690 para Gral Paz
from pprint import pprint
pprint(lista_de_parque)
'''
##############################################################

#ejercicio 3.19 Determinar las especies en un parque

##############################################################
'''
import csv
def leer_parque(nombre_archivo, parque):
	'abre el archivo indicado y devuelve una lista de diccionarios con la información del parque especificado'
	with open(nombre_archivo, 'rt') as f:
		lista_parque = []
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record=dict(zip(headers, row))  #armo dicc con dict(zip)
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				if record['espacio_ve'] == parque:
					lista_parque.append(record)  #appendea los dicc a la lista camion
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return lista_parque

#usando SET
def especies(lista_arboles):
	'Toma una lista de árboles y devuelva el conjunto de especies'
	lista=[]
	for elemento in lista_arboles:
		lista.append(elemento['nombre_com'])
		conjunto=set(lista)
	return conjunto

#otra opcion: usando .add
#def especies(lista_arboles):
#	'Toma una lista de árboles y devuelva el conjunto de especies'
#	conjunto={}
#	for elemento in lista_arboles:
#		conjunto.add(elemento['nombre_com'])
#	return conjunto
	

parque='GENERAL PAZ'
lista_arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv',parque)
conjunto_especies=especies(lista_arboles)
#print(len(lista_de_parque)) #chequeo que sean 690 para Gral Paz
from pprint import pprint
pprint(lista_arboles)
print(conjunto_especies)
'''

##############################################################

#ejercicio 3.20 Determinar las especies en un parque

##############################################################


############
#FUNCIONES:
############

import csv
def leer_parque(nombre_archivo, parque):
	'abre el archivo indicado y devuelve una lista de diccionarios con la información del parque especificado'
	with open(nombre_archivo, 'rt') as f:
		lista_parque = []
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record=dict(zip(headers, row))  #armo dicc con dict(zip)
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				if record['espacio_ve'] == parque:
					lista_parque.append(record)  #appendea los dicc a la lista camion
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return lista_parque

#usando SET
def especies(lista_arboles):
	'Toma una lista de árboles y devuelva el conjunto de especies'
	lista=[]
	for elemento in lista_arboles:
		lista.append(elemento['nombre_com'])
		conjunto=set(lista)
	return conjunto

# lo mismo que la de arriba pero usando .add
#def especies(lista_arboles):
#	'Toma una lista de árboles y devuelva el conjunto de especies'
#	conjunto={}
#	for elemento in lista_arboles:
#		conjunto.add(elemento['nombre_com'])
#	return conjunto

from collections import Counter
def contar_ejemplares(lista_arboles):
	'dada la lista generada por leer_parque(), devuelve dicc con especies:cantidad'
	dicc = {}
	for elemento in lista_arboles:
		dicc[elemento['nombre_com']]+=1
	return dicc


################
#PROGRAMA PPAL:
################

parques_a_estudiar=['GENERAL PAZ', 'ANDES, LOS','CENTENARIO'] #aqui colocar los nombres de los parques de interes

#imprimo las especies y sus cantidades (en este caso las 5 mas frecuentes)
for parque in parques_a_estudiar:
	lista_arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv',parque)
	diccio=contar_ejemplares(lista_arboles)
#armo tablitas con formato para cada parque
	sep='-'
	print('\n')
	print(f'{sep*40:20s} \n {parque:^40s} \n {sep*40:20s}')
	for arbol, cant in diccio.most_common(5):
		print(f'{arbol:^20s} {cant:>10d}')


'''
#Imprime las salidas de las funciones para el parque GENERAL PAZ:
parque='GENERAL PAZ'
lista_arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv',parque)
conjunto_especies=especies(lista_arboles)
#print(len(lista_de_parque)) #chequeo que sean 690 para Gral Paz
from pprint import pprint
pprint(lista_arboles) #lista de diccionarios
pprint(conjunto_especies) #conjunto con especies
'''


