
#informe.py
#ejercicio 3.9-La función zip()

import csv
### FUNCIONES: ###
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

def leer_precios(nombre_archivo):
	'abre un archivo con el contenido de un camión, lo lee y devuelve la información como un diccionario'
	with open(nombre_archivo, 'rt') as f:

		dict_precios = {}
		rows = csv.reader(f)
		for row in rows:
# este try-except sirve en caso de que halla archivos con datos faltantes.
			try:
				dict_precios[row[0]] = float(row[1])
			except:
				#print(f'Hay una fila en blanco en el archivo')
				pass    # en vez de que me escriba que hay una fila en blanco, hago un pass para que siga
	return dict_precios


### PROGRAMA GENERAL: ###

# llamo a las funciones camion y dict_precios (de los ejercios 2.16 y 2.17)
camion=leer_camion('../Data/camion.csv') #crea una lista de diccionarios anda igual usando fecha_camion
dict_precios=leer_precios('../Data/precios.csv') #crea un diccionario
costo = 0.0
print(dict_precios)
recaudacion = 0.0
for fila in camion:   #me muevo en los elementos de la lista "camion" (que son diccionarios)
	costo += int(fila['cajones'])*float(fila['precio'])  #calculo el costo con la info de los elementos de camion
	recaudacion += float(dict_precios[fila['nombre']])*int(fila['cajones']) #calculo la recaudacion usando el dict_precios. Solo me interesan aquellos elementos que tambien estan en camion. Por eso los "busco" usando fila['nombre']. 

print('BALANCE:')
print(f'Costo del camion:{costo}')
print(f'Reacudacion del camion:{recaudacion}')

#imprimo balance:
ganancia=recaudacion-costo
if ganancia > 0:
	print(f'Hubo ganancia, y fue de: {ganancia:0.3f} ')
elif ganancia < 0:
	print(f'Hubo perdida, y fue de: {ganancia:0.3f} ')
else:
	print(f'No hubo ni perdida ni ganancia. Pues ganancia = {ganancia} ') #por si la ganancia justo da 0



