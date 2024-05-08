#burbujeo.py
#ejercicio 12.2

def ord_burbujeo(lista):
	'''ordena lista por el metodo de la burbuja '''
	
	n=len(lista)
	while n!=0:
		for i in range(n-1):
			if lista[i+1]<=lista[i]:   #compara elemento con su consecutivo, los da vuelta en caso que corresponda
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux
		n=n-1

	return lista

#complejidad del algoritmo: en la primera vuelta ahce n-1 comparaciones, en la segunda n-2, en la 3era n-3 etc. 
#sumando: n-1+n-2+n-3.... = 1/2(n^2-n)



#listas de prueba:
lista_1 = [1, 2, -3, 8, 1, 5]
print(ord_burbujeo(lista_1))
lista_2 = [1, 2, 3, 4, 5]
print(ord_burbujeo(lista_2))
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
print(ord_burbujeo(lista_3))
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]