#bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

tabela = pd.read_excel("cardio_train.xlsx")
print(tabela)

dados = tabela.loc[:,"cholesterol":"cardio disease"]
print(dados)

sns.pairplot(dados)
plt.show()

sns.heatmap(dados.corr(),annot=True,cmap="Blues_r")
plt.show()

#analise de aprendizado de máquina
x = dados.drop("cardio disease",axis=1)
y = dados["cardio disease"]

print(x)
print(y)

x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size = 0.30)

from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino.values, y_treino)

acuracia = pd.DataFrame([modelo.score(x_teste,y_teste)])
print(acuracia)

ldados = []
cholesterol = int(input("Nivel de colesterol alto? - 1- Sim/0 - Não"))
gluc = int(input("Nivel de glicose alta? 1 -Sim/ 0 - Não"))
smoke = int(input("Paciente fumante? 1 - Sim/ 0 - Não"))
Alco = int(input("Paciente alcoolico? 1 - Sim/ 0 -Não"))
physical_active = int(input("Pratica esportes? 1 - Sim/ 0 -Não"))

ldados.append(cholesterol)
ldados.append(gluc)
ldados.append(smoke)
ldados.append(Alco)
ldados.append(physical_active)


ldados=[ldados]

dados = pd.DataFrame(ldados,columns=["Colesterol alto","Glicose","Fumante","Alco","Praticante de exercicio"])
dados["Resultado"] = modelo.predict(dados)

print(dados)


