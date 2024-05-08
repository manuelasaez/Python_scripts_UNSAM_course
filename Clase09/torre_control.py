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


#encolo en self.items los aviones que quieren arribar
    def nuevo_arribo(self,avion):
        self.encolar(avion)

#armo una lista nueva para los aviones que quieren aterrizar
    def nueva_partida(self,avion,partidas=[]):
        self.lista_partidas=partidas
        partidas.append(avion)

    def ver_estado(self):
    	print(f'Vuelos esperando para aterrizar: {self.items}')
    	print(f'Vuelos esperando para despegar {self.lista_partidas}')

    def asignar_pista(self):
    	if not self.esta_vacia():
    		print(f'El vuelo {self.items[0]} aterrizó con éxito')
    		self.desencolar()
    	else:
    		if self.lista_partidas: 
    			for i,avion in enumerate(self.lista_partidas):
    				self.lista_partidas.pop(i)
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