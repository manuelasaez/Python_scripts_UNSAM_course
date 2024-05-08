
import random


def tirar(m): 
	'devuelve una lista con m dados generados aleatoriamente'
	tirada=[]
	for i in range(m):
		tirada.append(random.randint(1,6)) 

	return tirada


#CASO 1:
def generala_no_necesariamente_servida_1():
	'CASO 1: si en la primera tirada salen todos dados diferentes, tiro los 5 nuevamente'
	m = 5
	tirada = tirar(m)
	generala = False

	mano = 1
	#si no tengo aun generala, tiro dos veces mas:
	while mano <= 3 and generala == False:
		#me fijo si en la primer tirada, ya tengo generala
		if tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada [3] and tirada[3] == tirada[4]:
			generala = True
		#print(tirada,mano)
		#armo lista con conteos por dado repetido
		else:
			lista_repeticion = []
			for i in range(m):
				lista_repeticion.append(tirada.count(i+1)) 

			# repeticiones es la cantidad de veces que se repite el dado
			repeticiones = max(lista_repeticion)
			#dado es el numero que se repitio mas veces.
			dado = lista_repeticion.index(repeticiones)+1
			if repeticiones == 1:
				tirada = tirar(m)
			else:
				tirada_2 = [dado]*repeticiones
				tirada = tirada_2 + tirar(m-repeticiones)
			mano+=1

	return generala


#CASO 2:
def generala_no_necesariamente_servida_2():
	'CASO 2: si en la primera tirada salen todos dados diferentes, dejo uno (el mas chico en este caso) y tiro los 4 restantes'
	m = 5
	tirada = tirar(m)
	generala = False
	#me fijo si en la primer tirada, ya tengo generala
#	if tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada [3] and tirada[3] == tirada[4]:
#		generala = True
#	if generala == False:
	mano = 1
	#si no tengo aun generala, tiro dos veces mas:
	while mano <= 3 and generala == False:
		if tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada [3] and tirada[3] == tirada[4]:
			generala = True
		else:
			#armo lista con conteos por dado repetido
			lista_repeticion = []
			for i in range(m):
				lista_repeticion.append(tirada.count(i+1)) 

				# repeticiones es la cantidad de veces que se repite el dado
			repeticiones = max(lista_repeticion)
				#dado es el numero que se repitio max_value veces.
			dado = lista_repeticion.index(repeticiones)+1
			tirada_2 = [dado]*repeticiones
			tirada = tirada_2 + tirar(m-repeticiones)
			#me fijo si obtuve generala con esta neuva tirada, de manera de salir del while. Sino, sigo.

			mano+=1
	return generala


#por defecto, si todos los dados son distintos, la busqueda de repeticiones da siempre 1, con lo cual no hay maximo. Python se queda con el que correpsonde al valor mas chico.
#es decir, si en mi tirada son todos dados distintos, el programa se queda con el mas chico y tira los otros 4. 


N = 100000
G1 = sum([generala_no_necesariamente_servida_1() for i in range(N)])
prob1 = G1/N
print(f'CASO 1: si en la primera tirada salen todos dados diferentes, tiro los 5 nuevamente')
print(f'Tiré {N} veces, de las cuales {G1} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala en maximo 3 tiros mediante {prob1:.6f}.')

G2 = sum([generala_no_necesariamente_servida_2() for i in range(N)])
prob2 = G2/N
print(f'CASO 2: si en la primera tirada le salen todos dados diferentes, dejo uno y tiro los 4 restantes')
print(f'Tiré {N} veces, de las cuales {G2} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala en maximo 3 tiros mediante {prob2:.6f}.')

print('Conclusion:')
if prob2 > prob1:
	print(f'Si en la primer tirada todos los dados son distintos, es mejor guardar uno y tirar solo los 4 restantes')
else:
	print(f'Si en la primer tirada todos los dados son distintos, es mejor tirar los 5 dados nuevamente')


