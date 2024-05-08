
import csv
def leer_camion(nombre_archivo):
    'Lee el archivo y devuelve lista de diccionarios'
    camion=[]
    f=open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        camion += [{
                  'nombre': row[0],
                  'cajon': int(row[1]),
                  'precio' :float(row[2])
        }]
    f.close()            
    return camion

camion= leer_camion('../Data/camion.csv')


def leer_precios(nombre_archivo):
    'Lee un archivo y genera un diccionario'
    f=open(nombre_archivo, 'r')
    rows=csv.reader(f)
    ventas={}
    for row in rows:
        try:
            ventas[row[0]]=float(row[1])
        except:
            pass
    f.close()
    return ventas 

ventas=leer_precios('../Data/precios.csv')


balance= 0
costo_camion=0
recaudado=0
for i in camion:
    costo_camion += i['precio']*i['cajon']
    for k in ventas: 
        if i['nombre'] == k:
            recaudado += ventas[k]*i['cajon']
            balance +=ventas[k]*i['cajon']-i['precio']*i['cajon']
if balance <= 0:
    b='en balance hay perdida'
else:
    b='en balance hay ganancia'

print(f'El costo del camión fue {costo_camion}, lo recaudado en ventas {recaudado},{b} de {balance}')         
 