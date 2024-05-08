#datetime.py

import datetime
fecha_hora = datetime.datetime.now()
print(fecha_hora)
date_object = datetime.datetime.strptime('10/11/1989', '%d/%m/%Y')
fecha = datetime.date.today()
print(fecha,date_object)
timestamp = datetime.date.fromtimestamp(1326244364)
print('Fecha =', timestamp)
hoy = datetime.date.today()
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes
a = datetime.time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)
b = datetime.time(11, 34, 56)
c = datetime.time(hour = 11, minute = 34, second = 56)
d = datetime.time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
print(b,c,d)
print('hour =', d.hour)
print('minute =', d.minute)
print('second =', d.second)
print('microsecond =', d.microsecond)

from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3=t1-t2
print(t3)

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6=t4-t5
print(t6)