#arboles.py
#ejercicio 5.24

import os
import matplotlib.pyplot as plt
import csv
import numpy as np



def leer_arboles(nombre_archivo):
	'abre el archivo indicado y devuelve una lista de diccionarios con la info de todos los arboles'
	with open(nombre_archivo, 'rt') as f:
		arboleda = []
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record=dict(zip(headers, row))  #armo dicc con dict(zip)
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				arboleda.append(record)  #appendea los dicc a la lista camion
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return arboleda

#ejercicio 5.24
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
especie = 'Jacarandá'
def histograma(nombre_archivo,especie):
	arboleda = leer_arboles(nombre_archivo)
	#armo lista con alturas usando la info de la lista de dicc arboleda, para jacaranda.
	altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== especie]
	plt.hist(altos,bins=50)
	return plt.show()

hist=histograma(nombre_archivo,especie)

def scatterplot(nombre_archivo,especie):
	arboleda = leer_arboles(nombre_archivo)
	diam=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']== especie] #creo lista de diametros
	altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== especie] #creo lista de altos
	d=np.array(diam)
	h=np.array(altos)
	plt.scatter(d,h, c= 'm', alpha=0.2)
	plt.xlabel("diametro (cm)")
	plt.ylabel("alto (m)")
	plt.title("Relación diámetro-alto para Jacarandás")
	return plt.show()

scatter = scatterplot(nombre_archivo,especie)


#Ejercicio 4.21: Diccionario con medidas
#la funcion medidas_de_especies() me la compartio Irina san sebastian pues yo no la habia hecho. 

def medidas_de_especies(especies,arboleda):
	'Arma un diccionario que sus claves son las especies y los valores son una lista de tuplas'
	dic={}	
	for especie in especies:
		T=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie ]
		dic[especie]=T
	
	return dic

'''
#5.26 desarmando la lista de tuplas y armando listas

def scatterplot(nombre_archivo,especies):
	arboleda = leer_arboles(nombre_archivo)
	medidas = medidas_de_especies(especies,arboleda)
	altos = []
	diam = []
	for especie in especies:
		for x,y in medidas[especie]:
			altos.append(x)
			diam.append(y)
		d=np.array(diam)
		h=np.array(altos)
		plt.scatter(d,h, c= 'm', alpha=0.2)
		plt.xlabel("diametro (cm)")
		plt.ylabel("alto (m)")
		plt.xlim(0,230) 
		plt.ylim(0,60) 
		plt.title(f'Relación diámetro-alto para {especie}')
		plt.show()
#	return plt.show()
#ver de hacerlo armando un darray a partir de la lsita de tuplas de medidas[especie], y luego ahcer slicing para referirme a la componente de alturas y diam

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
prueba = scatterplot(nombre_archivo,especies)
'''

#5.26 con slicing

def scatterplot(nombre_archivo,especies):
	arboleda = leer_arboles(nombre_archivo)
	medidas = medidas_de_especies(especies,arboleda)
	arreglo = ['E','P','J'] #lista de arreglos
	d =['E','P','J'] #lista de los slicing para quedarme con diametro (d) o altura (h)
	h =['E','P','J']
	for i,especie in enumerate(especies):
		arreglo[i]=np.array(list(medidas[especie]))
		h[i]=arreglo[i][:,0]
		d[i]=arreglo[i][:,1]
		plt.figure(i)
		plt.scatter(d[i],h[i], c= 'm', alpha=0.2)
		plt.xlabel("diametro (cm)")
		plt.ylabel("alto (m)")
		plt.xlim(0,230) 
		plt.ylim(0,60) 
		plt.title(f'Relación diámetro-alto para {especie}')
		plt.show()
	#graficos superpuestos:
	plt.scatter(d[0],h[0], s= 70, c= 'm', alpha=0.2, label= 'Eucalipto')
	plt.scatter(d[1],h[1], s= 70, c= 'b', alpha=0.2, label = 'Palo borracho rosado')
	plt.scatter(d[2],h[2], s= 70, c= 'c', alpha=0.2, label = 'Jacarandá')
	plt.legend()
	plt.xlabel("diametro (cm)")
	plt.ylabel("alto (m)")
	plt.xlim(0,230) 
	plt.ylim(0,60) 
	plt.title(f'Relación diámetro-alto para \n {especies}')
	plt.show()
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
prueba = scatterplot(nombre_archivo,especies)