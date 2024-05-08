import pandas as pd
import matplotlib.pyplot as plt


#leo archivo usando el tiempo como indice
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#grafico desde 12-25-2014 en adelante
#df['12-25-2014':].plot()
#plt.xlabel('tiempo')
#plt.ylabel('alturas del agua [cm]')
#df['10-15-2014':'12-15-2014'].plot()
#plt.show()

dh = df['12-25-2014':].copy()

delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 0 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()