#pascal.py
#ejercicio 11.9

def pascal(n,k):
	'calcula el valor del casillero del triangulo de pascal que se encuentra en la fila n y la columna k'

#bordes y primer casillero valen 1
	if n==0 or k==0 or k==n:
		return 1

	suma=pascal(n-1,k-1)+pascal(n-1,k)
	return suma

#casos de prueba:
print(pascal(4,2))
print(pascal(1,2))

