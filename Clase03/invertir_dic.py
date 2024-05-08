#invertir_dic.py

precios = {
		'Pera' : 490.1,
		'Lima' : 23.45,
		'Naranja' : 91.1,
		'Mandarina' : 34.23
	}

print(precios.items())

lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)
print(precios.values())
print(sorted(lista_precios))