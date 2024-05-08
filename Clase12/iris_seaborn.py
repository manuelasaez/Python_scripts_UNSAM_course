#ejercicio 


from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_dataset = load_iris()



# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)


iris_dataframe['target'] = iris_dataset['target']

print(iris_dataframe.head(10))
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
#pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)


sns.pairplot(iris_dataframe, vars= ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], hue='target', height=2.5, diag_kind="hist", diag_kws={'hue' : None , 'bins':20})
plt.savefig('iris.pdf')
plt.show()
