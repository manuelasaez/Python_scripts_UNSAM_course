#lote.py


class Lote:
	"""docstring for ClassName"""
	def __init__(self, nombre, cajones, precio):
		self.nombre = nombre
		self.cajones = cajones
		self.precio = precio

	def costo(self):
		costo=int(self.cajones)*float(self.precio)
		return costo

	def vender(self,caj_vendidos):
		self.cajones-=caj_vendidos

	    # Used with `repr()`, ejercicio 9.9
	def __repr__(self):
		return f'Lote({self.nombre}, {self.cajones},{self.precio})'



