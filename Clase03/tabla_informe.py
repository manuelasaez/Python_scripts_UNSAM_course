#tabla_informes 3.13 y 3-14
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


#funcion hacer informe:

def hacer_informe(lista_camion, dict_precios):
	'Entran camion (lista de diccionarios) y precios (diccionario) y devuelve lista de tuplas'
	lista_informe=[]
	for fila in camion:   #me muevo en los elementos de la lista "camion" (que son diccionarios)
		cambio=float(precios[fila['nombre']])-float(fila['precio'])
		tupla=(fila['nombre'], int(fila['cajones']),float(fila['precio']),cambio)
		lista_informe.append(tupla)
	return lista_informe


def formato(headers):
	'funcion que segun el header, arma separador de guiones'
	separador=f'{"-"*10:>10s} '*len(headers)
	return separador

### PROGRAMA GENERAL: ###

costo = 0.0
recaudacion = 0.0

# llamo a las 3 funciones e imprimo tabla con f print
camion=leer_camion('../Data/camion.csv') #crea una lista de diccionarios anda igual usando fecha_camion
precios=leer_precios('../Data/precios.csv') #crea un diccionario
informe=hacer_informe(camion,precios)

#doy headers y llamo funcion separadores para armar la listita de guiones.
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
sep=formato(headers)

#3.15 agregar encabezados
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(sep)
for nombre, cajones, precio, cambio in informe:
	precio='$'+str(precio)  #solo logre que el $ me quede en la posicion deseada pasandolo a strig
	print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')