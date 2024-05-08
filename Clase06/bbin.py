#bbin.py
#ejercicio 6.14
def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve pos tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    var=True
    estaba = True  #queda en true si el elemento estaba en la lista
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            var=True
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            var=False
    if pos == -1:
        estaba=False #el elemento no estaba en la lista
        #print(f'El elemento {x} no esta en la lista, si lo quiere agregar ordenadamente, deberia ocupar la posicion:')
        if var==False: 
            pos=medio+1
        else:
           pos=medio
    else:
    	#print(f'La posicion donde se encuetra el elemento {x} es:')  #saque estos comentarios para que el ejercicio 6.15 no escriba de nuevo. 
    return pos,estaba




#6.15 

def insertar(lista, x):
	'''
	Recibe una lista ordenada y un elemento. Si el elemento se encuentra en la lista
	solamente devuelve su posición; si no se encuentra en la lista, 
	lo inserta en la posición correcta para mantener el orden. En este segundo caso, también debe devolver su posición.
	'''
	pos,var2 = donde_insertar(lista,x)
	print(pos)
	if var2 == False:
		lista.insert(pos,x)
	return pos



lista = [1,3,4,7]
e=9
#llamada del 6.14
#pos,estaba=donde_insertar(lista,e)
#print(pos,estaba)

#llamada del 6.15
posicion=insertar(lista,e)
print(f'la posicion donde debe ir el {e} es {posicion}')
print(f'La lista nueva es {lista}')



