##################################################################
#	PROGRAMAS COSTO CAMION-DISTINTAS VERSIONES
##################################################################

#costo_camion.py 2.2
'''
with open('../Data/camion.csv', 'rt') as f:
	headers = next(f).split(',')
	costo_tot = 0.0
	for line in f:
		row = line.split(',')  #arma una lista con los elem de string. separador=coma
		costo_tot += int(row[1]) * float(row[2])
	print(costo_tot)
'''
##################################################################
'''
#costo_camion.py 2.6 (usando funciones)
def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	with open(nombre_archivo, 'rt') as f:
		headers = next(f).split(',')
		costo_tot = 0.0
		for line in f:
			row = line.split(',')  #arma una lista con los elem de string. separador=coma
			costo_tot += int(row[1]) * float(row[2])
	return costo_tot

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
'''
##################################################################
'''
#costo_camion.py 2.6 (usando funciones + try-except)
def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	with open(nombre_archivo, 'rt') as f:
		headers = next(f).split(',')
		costo_tot = 0.0
		for line in f:
			row = line.split(',')  #arma una lista con los elem de string. separador=coma
			try:
				costo_tot += int(row[1]) * float(row[2])
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {line}', end = '')
	return costo_tot
costo=costo_camion('../Data/missing.csv')
print('Costo total:', costo)	
'''
##################################################################

#costo_camion.py 
#ejercicio 2.9 (usando funciones + try-except + biblioteca csv)
import csv
def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	with open(nombre_archivo, 'rt') as f:
		costo_tot = 0.0
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			try:
				costo_tot += int(row[1]) * float(row[2])
			except ValueError:
				print(f'Aviso: datos faltantes en la fila {row}', end = '')
	return costo_tot
costo=costo_camion('../Data/missing.csv')
print('Costo total:', costo)	

