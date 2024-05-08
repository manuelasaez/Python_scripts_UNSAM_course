#documentacion.py
#ejercicio 7.8

def valor_absoluto(n):
    '''Calcula valor absoluto de un numero n

    Pre: n debe ser un numero real (no imaginario)
    Pos: devuelve un numero real positivo (o cero)
    '''
    if n >= 0:
        return n
    else:
        return -n
#No hay iteracion, con lo cual no hay invariante de ciclo


def suma_pares(l):
    '''Calcula la suma de los números pares que haya en la lista l.

    Pre: l es una lista de numeros
    Pos: devuelve res, que es el valor de sumar todos los números pares de la lista. En caso de no haber ninguno, da 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
#invariante de ciclo: res siempre debe ser par (o cero).  

def veces(a, b):
    '''Calcula el producto a*b (a+a+a)

    Pre: b debe ser un entero, a debe ser un numero real
    Pos: devuelve el numero real res= b*a (sumar a, b veces)
    '''	
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        #print(abs(res)+a,abs(a))
        res += a
        nb -= 1
    return res
#un invariante de ciclo es: nb*a+res (que siempre da a*b). 
#otro invariante podria ser: abs(res)+a>=abs(a), (o abs(res)>abs(a) pero solo a partir de la segunda iteracion)


def collatz(n):
    '''Calcula la conjetura 3n+1 de Collatz. Dado un numero entero positivo, si el número es par, divide por 2
       si el numero es impar multiplica por 3 y suma 1. Devuelve el num de iteraciones necesarias para llegar a 1. 

    Pre: numero entero positivo
    Pos: devuelve res, el num de iteraciones hasta que n=1. 
    '''	
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
# invariante de ciclo: n siempre es entero positivo
#otro invariante de ciclo: res>=1 siempre
#en las ultimas 3 iteraciones, n=4,2,1 siempre.

res=collatz(11)
print(res)