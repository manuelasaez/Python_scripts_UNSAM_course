#arboles.py


#Ejercicio 5.24 : genera un histograma con las alturas de los Jacarandás en el dataset

import csv
import os
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def leer_parque(nombre_archivo, parque):
	'Abre archivo, y devuelve la info como una lista de diccionarios con la info del parque indicado'
	f = open(nombre_archivo)
	rows = csv.reader(f)
	headers = next(rows)
	dic_parque = []
	for n_fila, row in enumerate(rows, start=1):
		record = dict(zip(headers,row))
		if record['espacio_ve']==parque:
			try:
				dic_parque.append(record) #está haciendo la lista de diccionarios
			except ValueError:
				print(f'Fila {n_fila}: No pude interpretar: {row}')
	f.close()
	return dic_parque

def leer_arboles(nombre_archivo):
	'Abre archivo, y devuelve la info como una lista de diccionarios con la info de todos los árboles en el archivo'
	f = open(nombre_archivo)
	rows = csv.reader(f)
	headers = next(rows)
	arboleda = []
	for n_fila, row in enumerate(rows, start=1):
		record = dict(zip(headers,row))
		try:
			arboleda.append(record) #está haciendo la lista de diccionarios
		except ValueError:
			print(f'Fila {n_fila}: No pude interpretar: {row}')
	f.close()
	return arboleda	

def especies(lista_arboles):
	'Ingresa una lista de árboles con sus características (lista de diccionarios) y devuelve un conjunto con las especies'
	esp=[]
	for row in lista_arboles:
		esp.append(row['nombre_com'])
	return set(esp)

def contar_ejemplares(lista_arboles):
	'Ingresa una lista de árboles con sus características (lista de diccionarios) y devuelve un diccionario con especies diccionario en el que las especies (claves) y la cantidad de ejemplares en esa especie (valor)'
	cantidad = Counter()
	for row in lista_arboles:
		cantidad[row['nombre_com']] += 1
	return cantidad


def obtener_alturas(lista_arboles, especie):
	'Ingresando una lista de árboles (lista de diccionarios) y una especie devuelve una lista con las alturas'
	altura=[]
	for row in lista_arboles:
		if row['nombre_com']==especie:
			altura.append(float(row['altura_tot']))
	return altura


def obtener_inclinaciones(lista_arboles, especie):
	'Dada una especie de árbol y una lista de árboles devuelve una lista de inclinaciones de esas especies'
	inclinaciones=[]
	for row in lista_arboles:
		if row['nombre_com']==especie:
			inclinaciones.append(float(row['inclinacio']))
	return inclinaciones


def especimen_mas_inclinado(lista_arboles):
	'Dada una lista de árboles devuelve la especie que tiene el ejemplar más inclinado y su inclinación'
	comparacion=[]
	mayor_inclinacion=()
	esp=especies(lista_arboles)
	for i in esp:
		#print(obtener_inclinaciones(lista_arboles,i)
		incl=max(obtener_inclinaciones(lista_arboles,i))
		#max_incl=max(incl)
		tupla=(incl,i)
		comparacion.append(tupla)
	mayor_inclinacion=max(comparacion)
	return mayor_inclinacion


def especie_promedio_mas_inclinada(lista_arboles):
	'Dada una lista de árboles devuelve la especie que en promedio es la que tiene mayor inclinación, y el promedio'
	comparacion=[]
	mayor_promedio=()
	esp=especies(lista_arboles)
	for i in esp:
		incl=obtener_inclinaciones(lista_arboles,i)
		prom=sum(incl)/len(incl)
		tupla=(prom,i)
		comparacion.append(tupla)
	mayor_promedio=max(comparacion)	
	return mayor_promedio


#arboleda=leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

#print(arboleda)

#Ejercicio 4.19:Lista de altos de Jacarandá

#H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#Ejercicio 4.20: Armar una tupla con altura y diámetro del jacarandá

#T=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#Ejercicio 4.21: Diccionario con medidas

def medidas_de_especies(especies,arboleda):
	'Arma un diccionario que sus claves son las especies y los valores son una lista de tuplas'
	dic={}	
	for especie in especies:
		T=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie ]
		dic[especie]=T
	#dic={dic[especie]:[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie ]}
	#dic={especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie ] for especie in especies}
	return dic


#especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#dic=medidas_de_especies(especies,arboleda)

def histograma_altos(especie):
	'Genera un histograma con las alturas de la especie elegida'
	archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
	arboleda= leer_arboles(archivo)
	altos=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie] #creo la lista de altos
	plt.hist(altos,bins=50)
	return plt.show()



#hist_altos=histograma_altos('Jacarandá')

#Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás


def scatterplot(especie):
	'Genera un scatterplot de diámetro vs alto de la especie elegida'
	archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
	arboleda= leer_arboles(archivo)
	H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá'] #creo la lista de altos
	h=np.array(H) #cambio la lista a un array
	T=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá'] #creo la lista de diámetros
	t=np.array(T) #cambio la lista a un array
	plt.scatter(t,h, c='c', alpha=0.3) #ploteo diámetro vs altura, con color cian y transparencia
	plt.xlabel("diametro (cm)")
	plt.ylabel("alto (m)")
	plt.title(f'Relación diámetro-alto para {especie}')
	return plt.show()

scatterplot('Jacarandá')




