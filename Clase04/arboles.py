#arboles.py
#ejercicio 4.18
import csv

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

arboleda=leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
from pprint import pprint
#pprint(arboleda)

#ejercicio 4.19
#armo lista con alturas usando la info de la lista de dicc arboleda, para jacaranda.
H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
print(H)

#ejercicio 4.20
#armo lista de tuplas con (altura,diametro) usando la info de la lista de dicc arboleda, para jacaranda. 
H_D=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
print(H_D)