import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



notas = pd.Series([2, 7, 5, 10, 6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])

print notas.values

print notas.index

print notas["Julia"]

print notas.describe()

print("\n")

print np.log(notas)

df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas':[3, 4, 2, 1 ,4],
                   'Prova':[2, 7, 5, 10, 6],
                   'Seminario':[8.5, 7.5, 9.0, 7.5, 8.0]})
print(df)

print(df.dtypes)

print(df.columns)
print(df["Seminario"])
print df.describe()

print df.sort_values(by="Seminario")

print df.loc[3]
print df[df["Seminario"]>8.0]
print df[(df["Seminario"]>8.0) & (df["Prova"]>3)]

df = pd.read_csv("matriz_01.csv")
print(df)
print df.describe()
print df.head()
print df.tail()
print df["951709"].unique()
print df["951709"].value_counts()
print df.isna()

plt.plot([10,20,30,40],[15,40,75,90],linestyle='--',color='r',marker='s',linewidth=3.0)
plt.axis([0,50,0,100])
plt.show()

y_axis = [20,50,30]
x_axis = range(len(y_axis))
width_n = 0.4
bar_color = 'yellow'
plt.bar(x_axis,y_axis,width = width_n,color=bar_color)
plt.show()

