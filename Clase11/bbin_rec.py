#bbin_rec.py
#ejercicio 11.11


def bbinaria_rec(lista, e):
    '''realiza búsqueda binaria de un elemento e en una lista ordenada lista. Devuelve True o False si lo encuentra o no'''

    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2

        if e >= lista[medio]:
            res = bbinaria_rec(lista[medio:],e)	

        else:
            res = bbinaria_rec(lista[:medio],e)	
            
    return res

#lista de prueba para testear
lista=[1,2,5,3,8,11,7]
lista_ord=sorted(lista)
e=15
encuentra=bbinaria_rec(lista_ord,e)
print(encuentra)