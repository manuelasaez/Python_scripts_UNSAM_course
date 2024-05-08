#torre_control.py
#ejercicio 9.12

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl(Cola):

    def nuevo_arribo(self,avion,arribos=[]):
        self.lista_arribos=arribos
        arribos.append(avion)

    def nueva_partida(self,avion):
        self.encolar(avion)

    def ver_estado(self):
    	print(f'Vuelos esperando para aterrizar: {self.lista_arribos}')
    	print(f'Vuelos esperando para despegar {self.items}')

    def asignar_pista(self):
    	while self.lista_arribos:
    		print(f'El vuelo {self.lista_arribos[-1]} aterrizó con éxito')
    		self.encolar(self.lista_arribos.pop(-1))

    	if self.items: 
    		l=(len(self.items)-2)
    		for avion in self.items[:l]:
    			self.desencolar()
    			print(f'El vuelo {avion} despego con éxito')
    	else:
    		print('No hay vuelos en espera')


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.ver_estado()
print(torre.items)