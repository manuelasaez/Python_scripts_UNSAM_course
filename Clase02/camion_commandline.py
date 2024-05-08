import csv
import sys
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
				print(f'Aviso: datos faltantes en la fila {row}')
	return costo_tot


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
costo=costo_camion(nombre_archivo)
print('Costo total:', costo)	

