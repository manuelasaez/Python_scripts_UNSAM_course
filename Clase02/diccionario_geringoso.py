######################################################
#diccionario_geringoso.py
######################################################
# ejercicio 2.14
#Opcion A: Usando la funcion dict()
'''
def geringoso(cadena):
	capadepenapa = ''
	for c in cadena:
		if c in 'aeiou':
			c=c+'p'+c
		capadepenapa=capadepenapa + c
	return capadepenapa
lista2 = []
lista1 = ['banana', 'manzana', 'mandarina']
for palabra in lista1:
	gerin = geringoso(palabra)
	lista2.append(gerin)
d = dict(zip(lista1,lista2))
print(d)

'''
######################################################

# ejercicio 2.14
# Opcion B: creandolo a partir de un dict vacio
def geringoso(cadena):
	capadepenapa = ''
	for c in cadena:
		if c in 'aeiou':
			c=c+'p'+c
		capadepenapa=capadepenapa + c
	return capadepenapa

d = {}
lista = ['banana', 'manzana', 'mandarina']
for palabra in lista:
	gerin = geringoso(palabra)
	d[palabra]=gerin
print(d)

######################################################