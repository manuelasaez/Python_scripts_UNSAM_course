#xaternidad.py
#ejercicio 8.3

from datetime import datetime, date, timedelta


def dias_para_incorporacion():
	'''Calcula dias que restan para incorporacion luego de 200 dias de licencia '''
	inicio_licencia = date(year = 2020, month = 9, day = 26)
	hoy = date.today()
	fin=inicio_licencia +timedelta(days = 200)
	return fin

print(dias_para_incorporacion())