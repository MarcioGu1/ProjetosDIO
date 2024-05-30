import pyautogui as py
from datetime import time
from time import sleep
import pandas as pd
import openpyxl
from openpyxl import Workbook,load_workbook
import plotly.express  as px
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv('clientes.csv')
df1=pd.read_csv('novos_clientes.csv')

#preparando o dataframe
codificador = LabelEncoder()
#tranforma texto em numero codificado
df['profissao'] = codificador.fit_transform(df['profissao'])
df['mix_credito']= codificador.fit_transform(df['mix_credito']) 
df['comportamento_pagamento'] = codificador.fit_transform(df['comportamento_pagamento'])

#Quem vou usar? x=dataframe
x= df.drop(columns=["score_credito",'id_cliente'])
#Quem eu quero prever? Y=(score_credito)
y= df['score_credito']

#dados de treino / dados de teste
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

#criando IA
#1º importa ela
#2º cria 
#3º treina ela
#arvore de decisão
#KNM  - > Vizinhos proximos - > Nearest neighbors

modelo_arvore = RandomForestClassifier()
modelo_Knm = KNeighborsClassifier()

#treinando-a
modelo_arvore.fit(x_treino,y_treino)
modelo_Knm.fit(x_treino,y_treino)

#testas modelos
previsao1=modelo_arvore.predict(x_teste )
previsao2=modelo_Knm.predict(x_teste )

#prevendo resultados
print(df1)
df1['profissao'] = codificador.fit_transform(df1['profissao'])
df1['mix_credito']= codificador.fit_transform(df1['mix_credito']) 
df1['comportamento_pagamento'] = codificador.fit_transform(df1['comportamento_pagamento'])

previsao= modelo_arvore.predict(df1)
print(previsao)