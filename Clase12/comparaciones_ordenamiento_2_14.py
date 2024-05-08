#comparaciones_ordenamiento.py
#ejercicio 12.4

import random

#############ORDENAMIENTO POR BURBUJA:
def ord_burbujeo(lista):
	'''ordena lista por el metodo de la burbuja '''
	cont=0
	n=len(lista)
	while n!=0:
		for i in range(n-1):
			if lista[i+1]<=lista[i]:   #compara elemento con su consecutivo, los da vuelta en caso que corresponda
				cont+=1
				aux=lista[i]
				lista[i]=lista[i+1]
				lista[i+1]=aux
		n=n-1

	return lista,cont


#############ORDENAMIENTO POR SELECCION:
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    cont=0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        #cont+=1
        # posición del mayor valor del segmento
        p,c = buscar_max(lista, 0, n,cont)
        cont=c
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return cont

def buscar_max(lista, a, b,cont):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
            cont+=1
    return pos_max,cont



#############ORDENAMIENTO POR INSERCION:
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    cont=0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            cont+=1
            reubicar(lista, i + 1,cont)
        #print("DEBUG: ", lista)
    return cont

def reubicar(lista, p,cont):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        cont+=2
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return cont

############################

def generar_lista(N):
    lista = [0]  * N
    for i in range(N):
        lista[i] = random.randint(1,1000)
    return lista


random.seed(15)
print(generar_lista(3))




k=100 #cantidad de listas
N=10
sum_cont_s=0
random.seed(15)
for i in range(k):
	lista=generar_lista(N)
	cont=ord_seleccion(lista)
	sum_cont_s+=cont

cont_prom_s=sum_cont_s/k
print(f'contador promediado en 100 lista para metoso seleccion: {cont_prom_s}')

sum_cont_i=0
random.seed(15)
for i in range(k):
	lista=generar_lista(N)
	cont=ord_insercion(lista)
	sum_cont_i+=cont

cont_prom_i=sum_cont_i/k
print(f'contador promediado en 100 lista para metoso inserción: {cont_prom_i}')

sum_cont_b=0
random.seed(15)
for i in range(k):
	lista=generar_lista(N)
	lista,cont=ord_burbujeo(lista)
	sum_cont_b+=cont
print(sum_cont_b)
cont_prom_b=sum_cont_b/k
print(f'contador promediado en 100 lista para metodo burbuja: {cont_prom_b}')


