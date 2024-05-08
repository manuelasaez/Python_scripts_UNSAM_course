#Ejercicio 5.8

import numpy as np
import matplotlib.pyplot as plt


temperaturas = np.load('../Data/Temperaturas.npy')
plt.hist(temperaturas,bins=75)
plt.show()

