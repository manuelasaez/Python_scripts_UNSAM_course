#arbolado_parques_veredas.py
#ejercicio 8.9


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#armo los paths
directorio = '../Data'
archivo_veredas='arbolado-publico-lineal-2017-2018.csv'
archivo_parques='arbolado-en-espacios-verdes.csv'
fname_v = os.path.join(directorio,archivo_veredas)
fname_p = os.path.join(directorio,archivo_parques)

#cargo las tablas en dos dataframes
df_veredas = pd.read_csv(fname_v)
df_parques = pd.read_csv(fname_p)

#selecciono las columnas de interes
cols_sel_v = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
cols_sel_p = ['nombre_cie', 'diametro' , 'altura_tot']
df_veredas_sel = df_veredas[cols_sel_v].copy()
df_parques_sel = df_parques[cols_sel_p].copy()

#me quedo solo con la fila correspondiente a tipas:
df_tipas_veredas=df_veredas_sel[df_veredas_sel['nombre_cientifico'] == 'Tipuana tipu']
df_tipas_parques=df_parques_sel[df_parques_sel['nombre_cie'] == 'Tipuana Tipu']


df_tipas_parques=df_tipas_parques.rename(columns={"nombre_cie":"nombre_cientifico","diametro": "Diametro", "altura_tot": "Altura"})
df_tipas_veredas=df_tipas_veredas.rename(columns={"diametro_altura_pecho": "Diametro", "altura_arbol": "Altura"})
df_tipas_parques['ambiente']='parque'
df_tipas_veredas['ambiente']='vereda'

#junto ambos dataframes en uno:
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#hago box-plots
'''A box plot is a method for graphically depicting groups of numerical data through their quartiles. 
The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). 
The whiskers extend from the edges of box to show the range of the data. 
The position of the whiskers is set by default to 1.5 * IQR (IQR = Q3 - Q1)
from the edges of the box. Outlier points are those past the end of the whiskers.'''
df_tipas.boxplot('Diametro', by = 'ambiente')
df_tipas.boxplot('Altura', by = 'ambiente')

plt.show()
#print(df_tipas)


#si quisiera seleccionar mas de una especie, puedo armar una lista "especies_seleccionadas" con las que me interesan y hacer: 
#df_seleccion = df_veredas_sel[df_veredas_sel['nombre_cientifico'].isin(especies_seleccionadas)]