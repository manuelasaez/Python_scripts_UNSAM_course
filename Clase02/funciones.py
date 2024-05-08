#pruebas
'''
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a=sumcount(10)
print(a)


import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
'''
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')


