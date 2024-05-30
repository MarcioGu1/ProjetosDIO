  
import pyautogui as py
from datetime import time,datetime
from time import sleep
import pandas as pd
#py.clik () = Clicar em algum lugar
#py.write() = escreve um texto
#py.press() = pressionar uma tecla 
#py.hotkey("crtrl",'v') =pressiona mais de uma tecla 
#py.PAUSE()= tempo ;cria uma pausa no sistema todo
#print(py.position()) = mostra as coordenadas do cursor
#py.scroll() = n+ vai pra cima,n- vai pra baixo
#abrir navegador
py.press("win")
py.write("chrome")
py.press("enter")
sleep(0.5)
#entra no site
link = "http://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
sleep(0.5)
py.press("enter")
sleep(3)
#cadastrando no site
py.click(x=348, y=353)
py.write('marcio')
py.press('tab')
py.write('marcio')
py.press('tab')
py.press('enter')
sleep(2)
#cadastrando produtos

#importando banco de dados
import pandas as pd
tabela =pd.read_csv('produtos.csv',sep = ',')
#for row in tabela:
#   for cell in row:
#        print (cell)
#cadastrando produto
py.click(x=654, y=382)
py.click(x=327, y=262)
#erro programa esta dando mais tab doq esperado
for row in tabela.index:
    py.write(tabela.loc[row,'codigo'])
    py.press('tab')

    py.write(tabela.loc[row,'marca'])
    py.press('tab')

    py.write(tabela.loc[row,"tipo"])
    py.press('tab')

    py.write(str(tabela.loc[row,"categoria"]))
    py.press('tab')
    
    py.write(str(tabela.loc[row,"preco_unitario"]))
    py.press('tab')

    py.write(str(tabela.loc[row,"custo"]))
    py.press('tab')

    if not pd.isna(tabela.loc[row,"obs"]):
        py.write(tabela.loc[row,"obs"])
    py.press('tab')
    
    #final sobe 
    py.press('enter')
    py.scroll(5000)
    py.click(x=327, y=262)
    
    