#camion.py

with open('../Data/camion.csv', 'rt') as f:
        data = f.read()
print(data)

with open('../Data/camion.csv', 'rt') as f:
	for line in f:
		print(line, end = '')

# le saco el header:
f = open('../Data/camion.csv', 'rt')
headers = next(f)
for line in f:
	print(line, end = '')

f.close()

#saco header y armo listas con las filas
f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
	row=line.split(',')
	print(row)

f.close()

import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')


