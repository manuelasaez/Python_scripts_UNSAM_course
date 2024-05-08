#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de SEMANTICA y estaba ubicado en el "if" pues cambiaba el valor de de True a False en cada letra,
#de manera que le return se producia devolviendo solo el valor True o False relacionado a la ultima letra de la cadena. 
#Ademas, tambien tiene el error de no reconocer las a mayusculas. 
#	Lo corregi dfiniendo una nueva variable booleana llamada x ue comienza siendo False. Y que en caso de cumplirse la condicion del if, cambie a True. 
#	Ademas agregue el .lower() para que si la cadena esta en mayuscula, la comparacion la haga pasando a minusculas. 
#    A continuación va el código corregido
def tiene_a(expresion):
	n = len(expresion)
	i = 0
	x = False
	while i<n:
		if expresion[i].lower() == 'a':
			x = True
		i += 1
	return x

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de SINTAXIS y estaba ubicado disritnos lados. Faltaban : en la definicion de la funcion, en el while y en el if. 
#Tambien faltaba un = para la comparacion y estaba mal escrita la palabra "False"
# lo corregi agregando los dos puntos que faltaban en esos 3 lugares, agregando el = y cambiando Falso por False. Le agregue el lower para que reconozca mayusculas.
def tiene_a(expresion):
	n = len(expresion)
	i = 0
	while i<n:
		if expresion[i].lower() == 'a':
			return True
		i += 1
	return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')




#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de EJECUCION, dado que la expresion a veces era un string y a veces un int (en el caso 1984)
#
def tiene_uno(expresion):
	expresion = str(expresion)
	n = len(expresion)
	i = 0
	tiene = False
	while (i<n) and not tiene:
		if expresion[i] == '1':
			tiene = True
		i += 1
	return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error era de tipo SEMANTICO, le faltaba un return de manera que la funcion devolvia "none" en vez de la suma pedida
# lo corregi agregando un return c
def suma(a,b):
	c = a + b
	return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.4. Función leer_camion()
#Comentario: El error era de tipo SEMANTICO, porque sobreescribia el diccionario, quedando guardada solo la ultima vez que entraba
# lo corregi cambiando de lugar la linea registro={}. La ubique adentro del for de manera que vacie lo ya guardado cada vez que entra.. 
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
	camion=[]
	with open(nombre_archivo,"rt") as f:
		filas = csv.reader(f)
		encabezado = next(filas)
		for fila in filas:
			registro={}
			registro[encabezado[0]] = fila[0]
			registro[encabezado[1]] = int(fila[1])
			registro[encabezado[2]] = float(fila[2])
			camion.append(registro)
	return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)



