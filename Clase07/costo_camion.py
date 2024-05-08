#costo_camion.py 
#ejercicio 7.3
import informe as inf

def costo_camion(nombre_archivo):
	'lee archivo y calcula costo total'
	camion=inf.leer_camion(nombre_archivo)
	costo_total=0
	for elemento in camion:
		costo_total+=elemento['cajones']*elemento['precio']

	return costo_total


def main(param):
	if len(param) != 2:
		raise SystemExit(f'Uso adecuado: {param[0]} ' 'archivo_camion')
	camion = param[1]
	print(f'El costo total del camion es {costo_camion(camion)}')

if __name__ == '__main__':
    import sys
    main(sys.argv)