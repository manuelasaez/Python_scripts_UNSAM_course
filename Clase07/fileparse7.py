#%%  EJERCICIO 6.9 con reemplazo de nombre_archivo por cualq iterable

import csv
def parse_csv(lines, select=None, types=None, has_headers=True):
    rows=csv.reader(lines)
    if has_headers: 
        headers= next(rows)
    if select:
        indices=[headers.index(nombre_columna) for nombre_columna in select]
        headers=select
    else:
        indices = []
    registros = []
    for row in rows:
        try:
            if not row:    # Saltear filas vacías
                continue
            if indices:    # Filtra si se especificaron columnas
                row=[row[index] for index in indices]
            if types:      #convierte los datos en tipo que quiero
                row= [func(val) for func,val in zip(types,row)]
            if has_headers:    #si hay headers armo diccionario, sino tupla
                registro = dict(zip(headers,row))
                registros.append(registro)
            else:
                registros.append(tuple(row))
        except ValueError as e:

                print(f'No pude convertir {row}')  #le pongo el +1, pues la fila 0 es el header
                print(f' Motivo: hay datos faltantes {e}')
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

