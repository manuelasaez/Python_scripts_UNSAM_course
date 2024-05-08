#costo_camion.py 
#ejercicio 7.3
import informe 

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(filename)
    return camion.precio_total()

def main(param):
	if len(param) != 2:
		raise SystemExit(f'Uso adecuado: {param[0]} ' 'archivo_camion')
	camion = param[1]
	print(f'El costo total del camion es {costo_camion(camion)}')

if __name__ == '__main__':
    import sys
    main(sys.argv)