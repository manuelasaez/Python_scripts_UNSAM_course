#alquiler.py
#ejercicio 11.14


import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    ''' ajuste por cuadrados minimos'''
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

''' da la relacion precio alquiler vs superficie en metros cuadrado para el barrio de Caballito CABA'''



superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie,alquiler)
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())


g = plt.scatter(superficie,alquiler)
plt.title('ajuste lineal relacion alquiler-metros en Caballito')
plt.plot(superficie, a*superficie+b, c = 'green')
plt.ylabel('alquiler [miles de pesos]')
plt.xlabel(r'superficie [$\rm{m}^2$]')

plt.show()

