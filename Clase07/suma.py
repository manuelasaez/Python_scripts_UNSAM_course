
#suma.py
#ejercicio 7.6
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma=0
    #hace la suma usando un ciclo.
    if desde <= hasta:
    	while desde <= hasta:
    		suma += desde
    		desde += 1 
    return suma



def sumar_enteros_2(desde,hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma=0
    #hace la suma usando sin usar ciclo. Usa suma triangular.
    if desde <= hasta:
    	suma=int(hasta*(hasta+1)/2-(desde-1)*(desde)/2)
    return suma



suma=sumar_enteros(-6,20)
print(f'usando un cilo, la suma es {suma}')
suma=sumar_enteros_2(-6,20)
print(f'sin usar cilco, la suma es {suma}')


#Un invariante en las sumas podria ser que abs(suma) >= abs(desde). 
#O (en caso que haya cilco) que abs(suma) en paso previo es menor que abs(suma) en paso siguiente.
