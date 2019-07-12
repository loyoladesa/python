import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



train_dataset = pd.read_csv('train.csv')
print(train_dataset.head())


tabela = pd.pivot_table(data=train_dataset,values='PassengerId',index='Sex',columns='Survived',aggfunc='count')
print tabela

#Array com os nao sobreviventes, dividios em male e female
bar_1 = tabela[0]

#Array com os sobreviventes, dividios em male e female
bar_2 = tabela[1]

#Range com a qauntidade de itens das barras
x_pos = np.arange(len(bar_1))

first_bar = plt.bar(x_pos,bar_1,0.5,color='b')
second_bar = plt.bar(x_pos,bar_2,0.5,color='y',bottom=bar_1)

# Definir posicao e labels no eixo X
plt.xticks(x_pos+0.25, ('Female','Male'))

plt.show()