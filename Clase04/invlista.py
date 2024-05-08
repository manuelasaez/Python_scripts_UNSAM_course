#Ejercicio 4.8: Invertir una lista
#invlista.py
def invertir_lista(lista):
	'ingresa una lista y la invierte'
	invertida = []
	i=0
	for e in lista: # Recorro la lista
		i+=-1
		invertida.append(lista[i])
	return invertida
lista1=[1,2,3]
lista2=['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
inv=invertir_lista(lista2)
print(inv)