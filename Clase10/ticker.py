#ticker.py
#ejercicio 10.10

from vigilante import vigilar
import csv
import formato_tabla

'''
def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows
'''

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

'''
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows
'''

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

#ejercicio 10.11
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila


'''
#10.10
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
'''


def ticker(camion_file, log_file, fmt):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''

    # Imprime el informe
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)
    formateador = formato_tabla.crear_formateador(fmt) #llama funcion dentro de formato_tabla.py que instancia mis objetos.
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for fila in filas:
        rowdata = [str(fila['nombre']), str(fila['precio']), str(fila['volumen'])]
        formateador.fila(rowdata)




#10.11
if __name__ == '__main__':
	import informe
	ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')






