# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append(lista[i])  #me borra el ultimo elemento de lista
    return invertida

l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

#%%
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
#%%
def propagar(lista):
	lista_propagada = list(lista)   #creo lista_propagada igual a la lista original pero en otro espacio de memoria (asi me queda tmb guardada la original), luego la ire cambiando
	i=0
	while i < (len(lista)-1):
		fosforo = lista[i]
		if (fosforo == 1 and lista[i+1]==0 and i != (len(lista)-1)):
			lista_propagada[i+1]=1
		elif (fosforo == 1 and lista[i-1]==0 and i != 0):
			lista_propagada[i-1]=1
		i+=1
		lista=lista_propagada
	return lista_propagada

lista =[0,1,-1,0,1,0]
lista=[ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
prop=propagar(lista)
print(prop,lista)


