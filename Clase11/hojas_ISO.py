#hojas_ISO.py
#ejercicio 11.13

def medida_hojas(n):
	'''Devuelve el tamaño en mm de la hoja A"n" '''

	if n==0:
		return 841, 1189

	else: 
		a=medida_hojas(n-1)[0]
		b=medida_hojas(n-1)[1]//2
		return b,a


print(medida_hojas(2))


