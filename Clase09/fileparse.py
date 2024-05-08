
#ejercicio 7.5
import csv
def parse_csv(f, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(f)
    if (not has_headers and select):
        raise RuntimeError('Para seleccionar, necesito encabezados')

    if has_headers:
            # Lee los encabezados del archivo
        encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
    for i,fila in enumerate(filas):

        try:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            if types:
                fila = [func(val) for func, val in zip(types, fila) ] 
                
            if has_headers:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                registros.append((tuple(fila)))
        except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i+1}: No pude convertir {fila}')  #le pongo el +1, pues la fila 0 es el header
                    print(f'Fila {i+1}: Motivo: hay datos faltantes {e}')
    return registros



def main():
    print('Pasandole linea:')
    lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    camion = parse_csv(lines, types=[str,int,float], has_headers = False)
    print(camion, '\n')

    print('Pasandole archivo zipeado:')
    import gzip
    with gzip.open('../Data/camion.csv.gz', 'rt') as file:
        camion = parse_csv(file, types=[str,int,float])
    print(camion, '\n')

    print('Pasandole archivo:')
    with open('../Data/camion.csv') as f:
        camion=parse_csv(f, types=[str,int,float])
    print(camion, '\n')



if __name__ == '__main__':
    main()