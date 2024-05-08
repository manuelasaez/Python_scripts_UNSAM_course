#costo_camion.py 
#ejercicio 6.12 (basado en el 2.9 de costo_camion.py de la clase 2).
#usa la funcion leer camion que desarrollamos en el programa informe_funciones.py
#import csv ya lo importa el modulo inf, asique no lo pongo mas. 

import informe_funciones as inf

def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	camion=inf.leer_camion(nombre_archivo)
	costo_total=0
	for elemento in camion:
		costo_total+=elemento['cajones']*elemento['precio']

	return costo_total

costo_total=costo_camion('../Data/camion.csv')

print(f'El costo total del camion es {costo_total}')


