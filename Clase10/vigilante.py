# vigilante.py
import os
import time

#Vigilante.py
#10.6

'''
def vigilar(nombre_archivo):
    #Generador que idica precios en el mercado en tiempo real, con indicación de qué producto se trata,
    # cuál es su precio, y cuál es el volumen de la operación (en cantidad de cajones)

    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line


if __name__ == '__main__':
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
'''
#vigilante.py 
#10.7

def vigilar(nombre_archivo):
    '''Generador que idica precios en el mercado en tiempo real, con indicación de qué producto se trata,
     cuál es su precio, y cuál es el volumen de la operación (en cantidad de cajones)'''

    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line

if __name__ == '__main__':
    import informe

    camion = informe.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
