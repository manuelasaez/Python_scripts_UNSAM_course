#ejercicio 4.9
#propaga.py
#%%
import copy

def propagar(lista):
	'recibe un vector con 0, 1 y -1 y devuelve un vector en el que los 1 se propagaron a sus vecinos con 0'
#creo lista_prop igual a la lista original pero en otro espacio de memoria (asi me queda tmb guardada la original). 
#Esto me ahorra cambiar los -1's y 1's pues de haber, quedan tal cual. Y solo resta cambiar 0's por 1's. 
	lista_prop = copy.deepcopy(lista)   

#recorro lista hacia adelante
	i = 0
	while i < (len(lista_prop)-1):  #recorro los elementos de la lista hasta el anteultimo
		if ( lista_prop[i] == 1 and lista_prop[i+1] == 0 ):  #me fijo si justo es 1 y si el elemento siguiente es 0. Ademas, NO entra si justo es el ulitmo elemento (pues no hay siguiente).
			lista_prop[i+1] = 1 #cambio el 0 por 1
		i += 1
#recorro lista hacia atras
	j = len(lista_prop)-1
	while j > 0:  #recorro los elementos de la lista hasta el primero
		if ( lista_prop[j] == 1 and lista_prop[j-1] == 0 ): #me fijo si justo es 1 y si el elemento anterior es 0. Ademas, NO entra si justo es el primer elemento (pues no hay anterior).
			lista_prop[j-1] = 1 #cambio el 0 por 1
		j -= 1
	
	return lista_prop

lista1 =[-1,0,0,0,0,1,0,-1,0,1]
lista2=[0,0,0,-1,1,0,0,0,-1,0,-1,0,0,0,0,1]
prop=propagar(lista2)
print('lista original', lista2)
print('lista propagada',prop)



