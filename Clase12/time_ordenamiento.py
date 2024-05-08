#


import time
import timeit as tt
import random
import numpy as np
import matplotlib.pyplot as plt
#############ORDENAMIENTO POR BURBUJA:
def ord_burbujeo(lista):
	'''ordena lista por el metodo de la burbuja '''
	n=len(lista)
	while n!=0:
		for i in range(n-1):
			if lista[i+1]<=lista[i]:   #compara elemento con su consecutivo, los da vuelta en caso que corresponda
				lista[i],lista[i+1]=lista[i+1],lista[i]
		n=n-1

	return lista

#############ORDENAMIENTO POR INSERCION:
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
           
        #print("DEBUG: ", lista)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


#############ORDENAMIENTO POR SELECCION:
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar

    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

################ORDENAMIENTO POR MERGE
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq= merge_sort(lista[:medio])
        der= merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)

    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

def generar_listas(Nmax):
	listas = []
	for N in range(1, Nmax):
		listas.append(generar_lista(N))
	return listas

def generar_lista(N):
    lista = [0]  * N
    for i in range(N):
        lista[i] = random.randint(1,1000)
    return lista

def experimento_timeit(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo= tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_merge= tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    
    return tiempos_seleccion,tiempos_insercion,tiempos_burbujeo,tiempos_merge



listas=generar_listas(256)

tiempos_seleccion,tiempos_insercion,tiempos_burbujeo,tiempos_merge = experimento_timeit(listas, 100)
plt.plot(tiempos_seleccion, label='seleccion')
plt.plot(tiempos_insercion,label='insercion')
plt.plot(tiempos_burbujeo,label='burbujeo')
plt.plot(tiempos_merge,label='merge')
plt.xlabel('longitud de la lista')
plt.ylabel('tiempo [s]')
plt.legend()
plt.savefig('tiempos_metodos_ordenamiento.pdf')
plt.show()
