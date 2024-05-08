#vida.py
from datetime import datetime, date


def segundos_vividos(fecha_nac):
	'''Calcula segundos vividos hasta la fecha actual a partir de la fecha de nacimiento ingresada '''
	date_object = datetime.strptime(fecha_nac, '%d/%m/%Y')
	hoy = datetime.today()
	delta=hoy-date_object #delta es un timedelta objetc
	print(type(delta))
	seg_de_vida=delta.total_seconds()
	return seg_de_vida

fecha_nac = input('Ingresá tu fecha de nacimiento en formato dd/mm/AAAA:')
print(f'La cantidad de segundos vividos desde tu nacimiento en fecha {fecha_nac} es de {segundos_vividos(fecha_nac)} segundos')
print(segundos_vividos(fecha_nac)/(60*60*24*365))
