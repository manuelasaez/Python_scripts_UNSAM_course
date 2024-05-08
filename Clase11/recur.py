def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

def factorial1(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    print(f)
    r = n * f
    return r



def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        print(p)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        print(p)
        return p * p * b

potencia(2,2)