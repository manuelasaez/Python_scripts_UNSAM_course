#informe_funciones.py
#tabla_informes con funciones 
#ejercicio 6.4


### FUNCIONES: ###
'''
def leer_camion(nombre_archivo):
	'
	Abre un archivo con el contenido de un camión, 
	lo lee y devuelve la información como una lista de diccionarios
	'
	import csv
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
	"""
	abre un archivo con el contenido de un camión, 
	lo lee y devuelve la información como un diccionario
	"""
	import csv
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


#funcion hacer informe:

def hacer_informe(camion, precios):
	'
	Entran camion (lista de diccionarios) y precios (diccionario) y devuelve lista de tuplas
	'
	lista_informe=[]
	for fila in camion:   #me muevo en los elementos de la lista "camion" (que son diccionarios)
		cambio=float(precios[fila['nombre']])-float(fila['precio'])
		tupla=(fila['nombre'], int(fila['cajones']),float(fila['precio']),cambio)
		lista_informe.append(tupla)
	return lista_informe


def formato(headers):
	'
	funcion que segun el header, arma separador de guiones
	'
	separador=f'{"-"*10:>10s} '*len(headers)
	return separador

def imprimir_informe(informe):
	'
	doy headers y llama funcion sep para armar la listita de guiones.
	e imprime la tabla correspondiente al informe
	'
	headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	sep=formato(headers)
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(sep)
	for nombre, cajones, precio, cambio in informe:
		precio='$'+str(precio)  #solo logre que el $ me quede en la posicion deseada pasandolo a strig
		print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


#ejercicio 6.5
def informe_camion(nombre_archivo_camion,nombre_archivo_precios):
	'
	Llama a las funciones leer_camion, leer_precios, hacer_informe e imprimir_informe
	para generar una tabla con el nombre de la fruta, la cantidad de cajones, el precio
	y la diferencia entre el valor comprado y el vendido.
	'
	camion=leer_camion(nombre_archivo_camion)
	precios=leer_precios(nombre_archivo_precios)
	informe=hacer_informe(camion,precios)
	imprimo=imprimir_informe(informe)
	return


informe_camion('../Data/camion.csv', '../Data/precios.csv')

#pruebo con otros archivos

files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
	print(f'{name:-^43s}')
	informe_camion(name, '../Data/precios.csv')
	print()
'''



#ejercicio 6.4


### FUNCIONES: ###

def leer_camion(nombre_archivo):
	'''
	Abre un archivo con el contenido de un camión, 
	lo lee y devuelve la información como una lista de diccionarios
	'''
	camion=fileparse.parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
	return camion


def leer_precios(nombre_archivo):
	"""
	abre un archivo con el contenido de un camión, 
	lo lee y devuelve la información como un diccionario
	"""
	lista_precios = fileparse.parse_csv(nombre_archivo, types = [str, float], has_headers = False)
	precios = dict(lista_precios)
	return precios


#funcion hacer informe:

def hacer_informe(camion, precios):
	'''
	Entran camion (lista de diccionarios) y precios (diccionario) y devuelve lista de tuplas
	'''
	lista_informe=[]
	for fila in camion:   #me muevo en los elementos de la lista "camion" (que son diccionarios)
		cambio=float(precios[fila['nombre']])-float(fila['precio'])
		tupla=(fila['nombre'], int(fila['cajones']),float(fila['precio']),cambio)
		lista_informe.append(tupla)
	return lista_informe


def formato(headers):
	'''
	funcion que segun el header, arma separador de guiones
	'''
	separador=f'{"-"*10:>10s} '*len(headers)
	return separador

def imprimir_informe(informe):
	'''
	doy headers y llama funcion sep para armar la listita de guiones.
	e imprime la tabla correspondiente al informe
	'''
	headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	sep=formato(headers)
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(sep)
	for nombre, cajones, precio, cambio in informe:
		precio='$'+str(precio)  #solo logre que el $ me quede en la posicion deseada pasandolo a strig
		print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


#ejercicio 6.5
def informe_camion(nombre_archivo_camion,nombre_archivo_precios):
	'''
	Llama a las funciones leer_camion, leer_precios, hacer_informe e imprimir_informe
	para generar una tabla con el nombre de la fruta, la cantidad de cajones, el precio
	y la diferencia entre el valor comprado y el vendido.
	'''
	camion=leer_camion(nombre_archivo_camion)
	precios=leer_precios(nombre_archivo_precios)
	informe=hacer_informe(camion,precios)
	imprimo=imprimir_informe(informe)
	return

import fileparse

informe_camion('../Data/camion.csv', '../Data/precios.csv')
