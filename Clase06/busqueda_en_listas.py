#busqueda_en_listas.py
#ejercicio 6.13
 
def busqueda_lineal_ordenada(lista,e):
	'''Si e está en la lista devuelve la posición de la primera vez que aparece, de lo
    contrario devuelve -1.
    '''
	pos = -1  # comenzamos suponiendo que e no está
	lista_ord=sorted(lista) #ordeno la lista
	for i, z in enumerate(lista_ord): # recorremos la lista ya ordenada
		if z == e:   # si encontramos a e
			pos = i  # guardamos la posición en la lsta ordenada por las dudas
			pos=lista.index(z) # guardamos su posición en la lsta no ordenada (la primera vez que aparece)
			print(z,pos)
		if z > e:
			break
	return pos

lista = [1,2,4,2,3,4]
e=4

posicion=busqueda_lineal_ordenada(lista,e)
if posicion != -1:
	print(f'La posicion donde se encuentra el elemento {e} por primera vez es: {posicion}')
else: 
	print(f'El elemento {e} no se ecuentra en la lista')

