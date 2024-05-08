
####################################################
'''
#Precio de la naranja.py 2.3
fruta='Naranja'  #aca poner la fruta a buscar el precio
f = open('../Data/precios.csv', 'rt')
for line in f:
	if fruta in line:
		precio_naran=line.split(',')[1]
		print(f'El precio de la naranja es: {precio_naran}')
f.close()
'''
#####################################################

#buscar_precio.py 2.7 (usando funcion)
def buscar_precio(fruta):
	'busca el precio de la fruta ingresada'
	with open('../Data/precios.csv', 'rt') as f:
		a = True  #para que entre o (NO) al print de cuando la fruta NO esta. Y lo haga solo una vez. 
		for line in f:
			if fruta == line.split(',')[0]:
				precio = line.split(',')[1]
				print(f'El precio de un cajon de {fruta} es: {precio}')
				a = False
	if a:
		print(f'{fruta} no figura en el listado de precios')

buscar_precio('Naranja')
