
#costo_camion.py 
#ejercicio 3.8 (costo cambion usando enumerate)
'''
import csv


def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	with open(nombre_archivo, 'rt') as f:
		costo_tot = 0.0
		filas = csv.reader(f)
		headers = next(filas)
		for n_fila, fila in enumerate(filas, start=1):
			try:
				costo_tot += int(fila[1]) * float(fila[2])
			except ValueError:
				print(f'Fila {n_fila}: No pude interpretar: {fila}')
	return costo_tot
costo=costo_camion('../Data/missing.csv')
print('Costo total:', costo)	
'''
################################################
#costo_camion.py 
#ejercicio 3.9 (costo cambion usando zip)
import csv
def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	with open(nombre_archivo, 'rt') as f:
		costo_total = 0.0
		filas = csv.reader(f)
		encabezados = next(filas)

		for n_fila, fila in enumerate(filas, start=1):
			record=dict(zip(encabezados, fila))
			try:
				ncajones = int(record['cajones'])
				precio = float(record['precio'])
				costo_total += ncajones * precio
			except ValueError:
				print(f'Fila {n_fila}: No pude interpretar: {fila}')
	return costo_total
#costo=costo_camion('../Data/missing.csv')
costo=costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)	



