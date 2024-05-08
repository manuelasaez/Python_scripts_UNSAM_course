#cadenas.py

count=0
cadena = "Ejemplo con for"
for c in cadena:
	if c=='o':
		count=count+1
	print('caracter:', c)
print('cantidad de letras o',count)


frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
lista_frutas = frutas.split(',')
print(lista_frutas)


for s in lista_frutas:
        print('s =', s)
