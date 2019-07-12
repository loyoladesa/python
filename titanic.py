import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data = {'pais': ['Brasil', 'Argentina','Argentina', 'Brasil', 'Chile','Chile'],
           'ano': [2005, 2006, 2005, 2006, 2007, 2008],
           'populacao': [170.1, 30.5, 32.2, 172.6, 40.8, 42.0]}
df = pd.DataFrame(df_data)
print(df)

train_dataset = pd.read_csv('train.csv')
print(train_dataset.head())
print train_dataset.Age
print (train_dataset.ix[3])
print(train_dataset.ix[[0,10,50]])
print(train_dataset[train_dataset.Sex == "female"])
tabela = pd.pivot_table(data=train_dataset,values='passengerId',index='Sex',columns='Survived',aggfunc='count')
print tabela