#primavera.py
#ejercicio 8.2

from datetime import datetime, date


def dias_para_primavera():
	'''Calcula segundos vividos hasta la fecha actual a partir de la fecha de nacimiento ingresada '''
	t1 = date(year = 2021, month = 9, day = 21)
	hoy = date.today()
	delta=t1-hoy #delta es un timedelta objetc
	return delta.days

primavera=dias_para_primavera()
print(f'Los dias que faltan para primavera son {primavera}')