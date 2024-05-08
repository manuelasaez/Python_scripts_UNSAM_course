### informe.py ###
#ejercicio 9.4


import formato_tabla
from lote import Lote
from camion import Camion
import fileparse

def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select=['nombre','cajones','precio'],
                                        types=[str,int,float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
	"""
	abre un archivo con el contenido de un camión, 
	lo lee y devuelve la información como un diccionario
	"""
	with open(nombre_archivo) as f:
		lista_precios = fileparse.parse_csv(f,  types = [str, float], has_headers = False)
		precios = dict(lista_precios)
	return precios


#funcion hacer informe:

def hacer_informe(camion, precios):
	'''
	Entran camion (lista de diccionarios) y precios (diccionario) y devuelve lista de tuplas
	'''
	lista_informe=[]
	for fila in camion:   #me muevo en los elementos de la lista "camion" (que son diccionarios)
		cambio=precios[fila.nombre]-fila.precio
		tupla=(fila.nombre, fila.cajones,fila.precio,cambio)  #
		lista_informe.append(tupla)
	return lista_informe


def formato(headers):
	'''
	funcion que segun el header, arma separador de guiones
	'''
	separador=f'{"-"*10:>10s} '*len(headers)
	return separador



#ejercicio 9.5
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt) #llama funcion dentro de formato_tabla.py que instancia mis objetos.
    imprimir_informe(data_informe, formateador)


def main(param):
	'''
	Funcion ppal. Entra con lista de 3 o 4 parametros (fmt es opcional).
	'''
	if len(param) != 3 and len(param) !=4:
		raise SystemExit(f'Uso adecuado: {param[0]} archivo_camion archivo_precios formato(txt,csv o html)')
	camion = param[1]
	precios = param[2]
	if len(param)==4:
		fmt= param[3]
		informe_camion(camion, precios,fmt) #si se aclara el formato se respeta el ingresado por terminal
	else: 
		informe_camion(camion, precios) #si no se pone nada, escribe en formato txt

if __name__ == '__main__':
    import sys
    main(sys.argv)

