#arbolado_lineal.py
#ejercicio 8.7
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

directorio = '../Data'
archivo='arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)


df = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal= df[cols_sel].copy()
cantidad_ejemplares=df_lineal['nombre_cientifico'].value_counts()

print(cantidad_ejemplares.head(10))
#selcciono 3 especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
#hago box-plots
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#pair plots usando seaborn

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
print(df_lineal_seleccion[cols_sel])

plt.show()