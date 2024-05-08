#informe_final.py incluye las funciones leer_camion y leer_precios y hace un balance de precios
#Ejercicio 2.18 Balances

'''En esta primera sección escribo las dos funciones que buscan en los archivos que están al final
leer_camion genera una lista de diccionarios con el nombre (key), cantidad de cajones y precios de las verduras del camion
leer_precios genera un diccionario con el nombre(key) y precios de las verduras del verdulero'''

import csv
#from pprint import pprint

def leer_camion(archivo):
    with open(archivo, 'rt', encoding = 'utf-8') as f:
        rows = csv.reader(f)    #lee el arhivo csv
        next(rows)              #salta la primer row que es la de los headers
        camion = []             #creo la lista donde se va a guardar el diccionario
        for row in rows:
            dic_camion = {}                     #para cada row el diccionario vuelve a arrancar así se guardan los nuevos valores
            dic_camion['nombre'] = row[0]       #para cada row se guarda el nombre de verdura(key)
            dic_camion['cajones'] = int(row[1])
            dic_camion['precio'] = float(row[2])
            camion.append(dic_camion)            #guarda el diccionario como nuevo elemento de la lista
    return camion

def leer_precios(archivo):
    with open(archivo, 'rt', encoding = 'utf-8') as f:
        rows = csv.reader(f)                     #lee el arhivo csv
        verdulero = {}                           #creo el diccionario donde guardo las verduras y sus precios
        for row in rows:
            if len(row) != 0:                    #solo para las row que contengan datos, si no tienen datos, la salta
                verdulero[row[0]] = row[1]       #para cada row se guarda el nombre de verdura(key) y el value el precio
            else:
                next
    return verdulero

#cargo los archivos camion y precio del directorio
camion = leer_camion('C:\Python32\Curso Python\ejercicios_python\Clase02\camion.csv')
verdulero = leer_precios('C:\Python32\Curso Python\ejercicios_python\Clase02\precios.csv')

#pprint(camion)
#pprint(verdulero)


#%%

'''En esta segunda sección se calculan los totales para el camion y para el verdulero, 
fue necesario buscar que verduras del verdulero, estaban en el camion y que habia diferentes cajones de la misma verdura
además se crean los diccionarios con los parciales de cada verdura
y el balance entre lo que vendio el verdulero y lo que compro del camion'''

verduras_verdulero = {}                   #diccionario con las verduras(que están en el camion) y el precio que el verdulero va a venderlas
dic_cajones_camion = {}                   #diccionario para guardar los cajones de verduras que hay en el camion
dic_parciales_camion = {}                 #diccionario para guardar los precios parciales de los cajones de verduras del camion
dic_parciales_verdulero = {}              #diccionario para guardar los precios parciales de los cajones de verduras del verdulero
balance_final = ''

total_camion = 0.0
for c in camion:                          #para conocer los precios totales de las verduras del camión, se repiten dos pero en el diccionario se guardan juntas
    parcial_camion = 0.0
    parcial_camion = c['cajones'] * c['precio']                 #el parcial de cada cajon de verdura
    total_camion += parcial_camion                              #el total de todas las verduras del camion
    
    if c['nombre'] not in dic_cajones_camion:
        dic_parciales_camion[c['nombre']] = parcial_camion          #genero un diccionario con los precios parciales de cajones para cada verdura
    else:
        dic_parciales_camion[c['nombre']] += parcial_camion         #como se repiten las naranjas y las mandarinas, tengo que sumar la cantidad de cajones de cada una
    
    if c['nombre'] not in dic_cajones_camion:
        dic_cajones_camion[c['nombre']] = c['cajones']          #genero un diccionario con el total de cajones para cada verdura
    else:
        dic_cajones_camion[c['nombre']] += c['cajones']         #como se repiten las naranjas y las mandarinas, tengo que sumar la cantidad de cajones de cada una
    
    
for verdu in dic_cajones_camion:                         #para cada key (verduras) del diccionario de cajones de verduras
    if verdu in verdulero:                               #si la verdura esta dentro de alguna de las key del diccionario verdulero
        verduras_verdulero[verdu] = verdulero[verdu]     #genera un diccionario con el precio que el verdulero va a vender las verduras(que están en el camion) 


total_verdulero = 0.0
for b in verduras_verdulero:
    parcial_verdulero = 0.0
    parcial_verdulero = float(verduras_verdulero[b]) * int(dic_cajones_camion[b])   #como los diccionarios estan ordenados, entonces multiplica la cantidad de cajones por el precio al que vende el verdulero
    total_verdulero += parcial_verdulero
    dic_parciales_verdulero[b] = parcial_verdulero
    
    
balance = total_verdulero - total_camion                    #el balance se calcula como la resta de lo que vendio el verdulero menos lo que compro del camion
if balance > 0:
    balance_final = "Hubo Ganancia"
else:
    balance_final = "Hubo Perdida"
#%%

'''Esta sección es para imprimir la tabla y que quede ordenada
linea_sep es una función que se puede modificar para escribir los - de la tabla del final'''

def linea_sep():
    print('-' * (10 + 20 + 22))

linea_sep()   

print(f'| {"Verdura":<10s} | {"Parcial Camion":^15s} | {"Parcial Verdulero":^16s} |')

linea_sep()

for a in dic_parciales_camion:
    print(f'| {a:<10s} | {dic_parciales_camion[a]:^15.2f} | {dic_parciales_verdulero[a]:^17.2f} |')
    
linea_sep()

print(f'| {"Totales":<10s} | {total_camion:^15.2f} | {total_verdulero:^17.2f} |')

linea_sep()

print(f'| {"Balance":<10s} | {balance:^15.2f}   {balance_final:^17} |')

linea_sep()