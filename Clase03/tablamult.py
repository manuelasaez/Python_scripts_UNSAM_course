#tablamult.py

def formato(headers):
	separador=f'{"-"*3:s}'*(len(headers)+1) #agrego uno por la columna de la izquierda que tiene los :

	return separador

#ARMO LISTA DE LISTAS CON LOS PRODUCTOS
lista_mult=[]
for n in range(10):
	lista=[0,0,0,0,0,0,0,0,0,0]
	lista_mult.append(lista) #me guarda lo que hay en lista dentro de lista_mult
	for i in range(1,10):
		lista[i]=lista[i-1]+n  #me sobreescribe la lista interna. Calculo los elementos sumando algo al anterior.

#ESCRIBO TABLA

h=list(range(10)) #arma lista h=[0,1,2,3,4,5,6,7,8,9]
print(f'    {h[0]:2d} {h[1]:2d} {h[2]:2d} {h[3]:2d} {h[4]:2d} {h[5]:2d} {h[6]:2d} {h[7]:2d} {h[8]:2d} {h[9]:2d}')
sep=formato(h)
print(sep)
for j,fila in enumerate(lista_mult):
	print(f'{j:2d}: {fila[0]:2d} {fila[1]:2d} {fila[2]:2d} {fila[3]:2d} {fila[4]:2d} {fila[5]:2d} {fila[6]:2d} {fila[7]:2d} {fila[8]:2d} {fila[9]:2d}')

#preguntar como hacer para darle formato a la lista, sin tener que ir componente a componente. 
#for fila in lista_mult:
#	out= ['{elem:.2d}' for elem in fila]
#	print(out)