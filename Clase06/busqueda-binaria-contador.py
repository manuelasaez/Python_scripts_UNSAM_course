#6.19
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        comps += 1 # sumo la comparación que estoy por hacer
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,comps


lista = [1,3,9,7,12,4]
lista_ordenada=sorted(lista)

print(f'La lista ordenada es {lista_ordenada}')
e=4
posicion,contador=busqueda_binaria(lista_ordenada,e)

if posicion != -1:
    print(f'La posicion donde se encuentra el elemento {e} por primera vez es: {posicion}')
else: 
    print(f'El elemento {e} no se ecuentra en la lista')

print(f'La cantidad de comparaciones realizadas para la busqueda fue de {contador}')