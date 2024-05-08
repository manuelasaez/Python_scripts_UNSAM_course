# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0


pago_extra_mes_comienzo = 60   #ver si esto va bien con mi contador que empieza en 0 y no en 1.
pago_extra_mes_fin = 107
pago_extra = 1000


while saldo > 0:

	if mes < 12:
		saldo = saldo * (1+tasa/12) - (pago_mensual)
		total_pagado = total_pagado + pago_mensual
		
	elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
		saldo = saldo * (1+tasa/12) - (pago_mensual+pago_extra)
		total_pagado = total_pagado + pago_mensual+pago_extra
		
	else:
		saldo1=saldo   #guardo para tener el valor antes de terminar el while y poder corregir el saldo
		total_pagado1=total_pagado
		saldo = saldo * (1+tasa/12) - pago_mensual
		total_pagado = total_pagado + pago_mensual

	if saldo <0:
		total_pagado=total_pagado1+saldo1
		saldo=0.0
	mes+=1

	print(mes, round(total_pagado, 2), round(saldo,2))
print('Total pagado', round(total_pagado, 2))
print('Meses totales:', mes)
