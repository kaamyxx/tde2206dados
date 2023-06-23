# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tbxept-RxRZyBZKZauHF1_Dtsd3EIp-q
"""

import pandas as pd

treino = pd.read_csv('train.csv')
treino.head(3)

pip install ydata-profiling

from ydata_profiling import ProfileReport

profile = ProfileReport(treino, title="titanic_treino")

profile.to_file("titanic_treino.html")

media_idade = titanic_treino['Idade'].mean()

sobreviventes = dados_passageiros[dados_passageiros['Sobreviveu'] == 1]
nao_sobreviventes = dados_passageiros[dados_passageiros['Sobreviveu'] == 0]

media_idade_sobreviventes = sobreviventes['Idade'].mean()

media_idade_nao_sobreviventes = nao_sobreviventes['Idade'].mean()

variancia_tarifa = dados_passageiros['Tarifa'].std() ** 2

variancia_tarifa_sobreviventes = sobreviventes['Tarifa'].std() ** 2

variancia_tarifa_nao_sobreviventes = nao_sobreviventes['Tarifa'].std() ** 2