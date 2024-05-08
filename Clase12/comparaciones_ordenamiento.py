#comparaciones_ordenamiento.py
#ejercicio 12.4

import random
import numpy as np
import matplotlib.pyplot as plt

#############ORDENAMIENTO POR BURBUJA:
def ord_burbujeo(lista):
	'''ordena lista por el metodo de la burbuja '''
	cont=0
	n=len(lista)
	while n!=0:
		for i in range(n-1):
			if lista[i+1]<=lista[i]:   #compara elemento con su consecutivo, los da vuelta en caso que corresponda
				lista[i],lista[i+1]=lista[i+1],lista[i]
			cont+=1
		n=n-1

	return lista,cont


#############ORDENAMIENTO POR SELECCION:
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    cont=0
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
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
        cont+=1
        if lista[i] > lista[pos_max]:
            pos_max = i
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
            c=reubicar(lista, i + 1,cont)
            cont=c
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
        cont+=1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return cont

################ORDENAMIENTO POR MERGE
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    cont=0
    cont2=0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq,cont = merge_sort(lista[:medio])
        der,cont = merge_sort(lista[medio:])
        lista_nueva,cont2 = merge(izq, der)

    cont+=cont2
    return lista_nueva,cont

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    cont2=0
    while(i < len(lista1) and j < len(lista2)):
        cont2+=3
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado,cont2

def generar_lista(N):
    lista = [0]  * N
    for i in range(N):
        lista[i] = random.randint(1,1000)
    return lista



k=1 #cantidad de listas para promedio (ejercicio 2.14 era con 100)
lista_i=[]
lista_s=[]
lista_b=[]
lista_m=[]
lista_fer=[]
for N in range(1,256):

	sum_cont_s=0
	random.seed(15)
	for i in range(k):
		lista=generar_lista(N)
		cont2=ord_seleccion(lista)
		sum_cont_s+=cont2
	
	cont_prom_s=sum_cont_s/k
	lista_s.append(cont_prom_s)
	
	
	sum_cont_i=0
	random.seed(15)
	for i in range(k):
		lista=generar_lista(N)
		cont3=ord_insercion(lista)
		sum_cont_i+=cont3
	
	cont_prom_i=sum_cont_i/k
	lista_i.append(cont_prom_i)

	
	sum_cont_b=0
	random.seed(15)
	for i in range(k):
		lista=generar_lista(N)
		lista,cont4=ord_burbujeo(lista)
		sum_cont_b+=cont4
	cont_prom_b=sum_cont_b/k
	lista_b.append(cont_prom_b)


	sum_cont_m=0
	random.seed(15)
	for i in range(k):
		lista=generar_lista(N)
		lista,cont5=merge_sort(lista)
		sum_cont_m+=cont5
	cont_prom_m=sum_cont_m/k
	lista_m.append(cont_prom_m)



comparaciones_insercion=np.array(lista_i)
comparaciones_seleccion=np.array(lista_s)
comparaciones_burbujeo=np.array(lista_b)
comparaciones_merge=np.array(lista_m)


plt.title('Comparacion metodos de ordenamiento')
plt.xlabel('Longitud de la lista')
plt.ylabel('Cantidad de comparaciones')
plt.plot(comparaciones_insercion, label='inserción')
plt.plot(comparaciones_seleccion, ls='--', label='selección')
plt.plot(comparaciones_burbujeo, ls=':', lw=5, label='burbuja')
plt.plot(comparaciones_merge, label='merge sort')

plt.legend()

plt.savefig('metodos_ordenamiento.pdf')
plt.show()


###########################
# NO TERMINO DE ENTENDER COMO CONTAR
# LAS COMPARACIONES.
# NO CREO QUE ESTEN BIEN LOS CONTADORES
#
##########################