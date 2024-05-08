#aproxiamr_pi.py
#ejercicio 5.4
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


N = 100000
M=0
for i in range(N):
	(x,y) = generar_punto()
	if (x**2+y**2) < 1: 
		M+=1

pi=4*M/N

print(f' La estimacion de pi usando {N} puntos es {pi} ') 
