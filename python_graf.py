from time import *
import pandas as pd
import numpy as np
from math import *
import matplotlib.pyplot as plt
import seaborn as sns
from time import *
import os

leitura = pd.read_csv("python_graf.csv")

#10 linhas e 4 colunas
#print(leitura.shape)

#primeiros dados
#print(leitura.head(10))

#há dados em nulo? se tiver me mostre em cada coluna a soma de itens em branco
#print(leitura.isnull().sum())

#abro uma varivel para armazenar a troca de valores que eu vou substituis dos null
modif = leitura['assinatura'].fillna(leitura['assinatura'].mean())
#printei pra confirmar a alteração
#print(modif)
#apliquei a alteração na coluna de assinatura
leitura['assinatura'] = modif

#print(leitura.head(10))
#mesmo processo da assinatura mas preenchendo com n
modifcan = leitura['cancelado'].fillna("n")

leitura['cancelado'] = modifcan

#contando numero de clientes cancelados e os não cancelados
cs = 0
cn = 0
scs = 0
for c in leitura['cancelado']:
    if c == "s":
        cs += 1

for c in leitura['cancelado']:
    if c == "n":
        cn += 1


#construindo um novo dataset para calcular financial churn, clientes somente com o item s de cancelado
churnvalue = leitura.loc[leitura['cancelado']=='s']
#somando assinatura dos cancelados
soma_churn = churnvalue['assinatura'].sum()

print("*"*30)
m = "Métricas"
print(f" {m:^27}")
print("*"*30)

sleep(3)
while True:
    try:
        print("""
        1 - Deseja ver o valor total de assinatura?
        2 - Deseja ver o valor medio de assinatura?
        3 - Deseja ver o logo churn?
        4 - Deseja ver o financial churn?
        5 - Deseja verificar uma descrição dos dados (assinatura)?
        6 - Deseja ver um gráfico de linha com valores gerais?
        7 - Deseja ver um gráfico de coluna com valores financial churn?
        8 - Deseja ver um gráfico de pizza com % de cancelado?
        9 - Deseja ver os dados?
        0- Para Sair""")

        esc = int(input("Digite o numero da opção que deseja, por favor"))
        sleep(3)
        if esc ==1:
            print(f"o valor total de assinatura é R${round(leitura['assinatura'].sum(),2)}")
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()
        if esc ==2:
            print(f" o valor médio de assinatura é R${round(leitura['assinatura'].mean())}")
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc ==3:
            print(f" o numero de clientes cancelados foi de {cs}")
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc ==4:
            print(f" o valor de financial churn dos clientes cancelados foi de {soma_churn} ")
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()
        if esc ==5:
            print(leitura['assinatura'].describe())
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc ==6:
            plt.figure(figsize=(10, 8))
            plt.plot(leitura['nome do cliente'],leitura['assinatura'])
            plt.ylabel("Assinatura")
            plt.xlabel("Clientes")
            plt.show()
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc ==7:
            plt.bar(churnvalue['nome do cliente'],churnvalue['assinatura'])
            plt.ylabel("Assinatura")
            plt.xlabel("Cliente")
            plt.show()
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc ==8:
            fatia = [cs,cn]
            labels = ["Cancelado", "Não-Cancelado"]
            colors=["orange","gray"]
            explode=[0,0,0]
            plt.pie(fatia,labels=labels,colors=colors,shadow=True,autopct = "%.2f%%")
            plt.legend()
            plt.show()
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()

        if esc==9:
            print(leitura.head(10))
            esco = input("Deseja ver outra métrica? - s/S para (Sim) - n/N para (Não)")
            if esco in 's/s':
                continue
            else:
                print("Obrigado por nos consultar!!!")
                exit()
        if esc >10:
            continue

        if esc ==0:
            print("Obrigado por nos Consultar!!")
            exit()

        if str(esc) in 'nN':
            exit()

    except ValueError:
        print("Escolha uma opção válida")
        continue


