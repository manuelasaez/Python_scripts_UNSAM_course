#inclusive.py

frase = 'todos somos programadores'
palabras = frase.split()
listafrase_t=[]
for palabra in palabras:
	if 'o' in palabra:
		pal1=palabra[0:-2]
		pal2=palabra[-2:].replace('o','e')
		pal=pal1+pal2
		listafrase_t.append(pal)    #agrego las palabras pasadas a inclusivo a la lista
	else:
		listafrase_t.append(palabra)    #esto lo tengo que poner para que tmb agregue aquellas palabras que no cambiarian 
frase_t=' '.join(listafrase_t)
print(frase_t)



