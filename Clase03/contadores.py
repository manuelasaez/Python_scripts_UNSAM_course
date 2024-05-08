#contadores.py

import csv
#FUNCIONES:
def leer_camion(nombre_archivo):
	'abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de diccionarios'
	with open(nombre_archivo, 'rt') as f:
		camion = []
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record=dict(zip(headers, row))  #armo dicc con dict(zip)
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				camion.append(record)  #appendea los dicc a la lista camion
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return camion
#leo archivos:
camion = leer_camion('../Data/camion.csv')
camion2 = leer_camion('../Data/camion2.csv')

#hago cosas con counter
from collections import Counter
tenencias = Counter()
for s in camion:
		tenencias[s['nombre']] += int(s['cajones'])

print(tenencias)
#Las 3 frutas con más cajones
print(tenencias.most_common(3))

#cuentas con camion2:
tenencias2 = Counter()
for s in camion2:
	tenencias2[s['nombre']] += int(s['cajones'])

print(tenencias2)

combinada = tenencias + tenencias2
print(combinada)