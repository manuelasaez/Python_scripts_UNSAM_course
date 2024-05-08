#geringoso.py

cadena = 'boligoma'
capadepenapa = ''
for c in cadena:
	if c in 'aeiou':
		c=c+'p'+c
	capadepenapa=capadepenapa + c
print(capadepenapa)