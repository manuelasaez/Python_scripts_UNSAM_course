#canguros_buenos.py
#ejercicio 9.11

class Canguro: 
	def __init__(self, nombre):
		"""Inicializar los contenidos del marsupio.
		contenido: contenido inicial del marsupio, lista.
		"""
		self.nombre = nombre
		self.contenido_marsupio = []


	def meter_en_marsupio(self,elemento):
		self.contenido_marsupio.append(elemento)

	def __str__(self):
		t = [ self.nombre + ' tiene en su marsupio:' ]
		if self.contenido_marsupio: #si la lista tiene cosas hace lo que sigue:
			for obj in self.contenido_marsupio:
			# me fijo si el objeto es un canguro u otra cosa.
				if isinstance(obj, Canguro):
					s ='    ' + object.__str__(obj.nombre)
				else:
					s='    ' + str(obj)
				t.append(s)
			return '\n'.join(t)
		else: # si la lista esta vacia:
			return f'{self.nombre} no tiene nada en su marsupio'			

madre_canguro=Canguro('madre')
cangurito=Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio(cangurito)
print(madre_canguro)
print(cangurito)


# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    def __init__(self, nombre):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []


    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        if self.contenido_marsupio:
            for obj in self.contenido_marsupio:
                s = '    ' + object.__str__(obj)
                t.append(s)
            return '\n'.join(t)
        else:
            return f'{self.nombre} no tiene nada en su marsupio'

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

# El problema que tenia el codigo canguros_malos era que en la funcion __init__ se tomaba como argumento por defecto contenido = []. 
#Y esto hacia que se vayan acumulando las pertencias de los objetos si se agreban cosas a la lista "contenido" previos a su creacion. 
#lo que hice fue explicitar el vaciado de la lista contenido_marsupio=[] cada ver que se crea un nuevo objeto. 
#De manera que todos comiencen con su lista vacia. El problema original era ademas que la lista siempre se llamaba igual (contenido) 
#de manera que al cambiar de un objeto a otro seguia llamandose igual y ya no usaba el valor por defecto de la funcion
# (pues si se habia hecho algun append, contenido ya tenia elmentos)  




