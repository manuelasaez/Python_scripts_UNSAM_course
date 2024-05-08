#ejercicio 4.9
#propaga.py
#%%
import copy

def propagar(lista):
	'recibe un vector con 0, 1 y -1 y devuelve un vector en el que los 1 se propagaron a sus vecinos con 0'
	lista_propagada = copy.deepcopy(lista)   #creo lista_propagada igual a la lista original pero en otro espacio de memoria (asi me queda tmb guardada la original), luego la ire cambiando
	n=0
	while n < len(lista):
		i=0
		while i < (len(lista)-1):  #recorro los elementos de la lista hasta el anteultimo

			fosforo = lista[i]  #estudio el elemento i al que le llamo fosforo.
			if (fosforo == 1 and lista[i+1]==0 and i != (len(lista)-1)):  #me fijo si justo es 1 y si el elemento siguiente es 0. Ademas, NO entra si justo es el ulitmo elemento (pues no hay siguiente).
				lista_propagada[i+1]=1 #cambio el cero por 1
			if (fosforo == 1 and lista[i-1]==0 and i != 0): #me fijo si justo es 1 y si el elemento anterior es 0. Ademas, NO entra si justo es el primer elemento (pues no hay anterior).
				lista_propagada[i-1]=1 #cambio el cero por 1
			if lista[len(lista)-1] ==1 and lista[len(lista)-2]==0:  #estudio ultimo elemento
				lista_propagada[len(lista)-2]=1 #cambio el cero por 1		
			i+=1
		lista=lista_propagada #actualizo la lista 
		n=n+1
		
	return lista_propagada

lista =[-1,0,0,0,0,1,0]
#lista=[ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, -1, 0,0,0, 0,1]
prop=propagar(lista)
print('lista original', lista)
print('lista propagada',prop)



