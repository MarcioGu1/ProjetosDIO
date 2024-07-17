"""
programa que ira reconhecer a voz do user
e realizar comando no sistema operaconal

"""

#importando bibliotecas
from selenium import *
import pyautogui as py
import pyttsx3

import os 
import speech_recognition as sr
import time

class Assistent:
    def __init__(self):
        self.falar("oi")

    # Função para o Friday  falar
    def falar(self,frase):
        engine = pyttsx3.init()
        engine.say(frase)
        engine.runAndWait()

    #Função para reconhecer a voz
    def ouvir_microfone(self):
        #Habilita o microfone
        microfone = sr.Recognizer()

        #Usando o microfone
        with sr.Microphone() as source:

            #Chama um algoritimo de redução de ruidos
            microfone.adjust_for_ambient_noise(source)

            self.falar("Estou te ouvindo senhor pode falar...")

            #Armazena o comando em variavel
            audio = microfone.listen(source)
            return audio,microfone
    def tarefas(self,audio,microfone):        
        try:

            #passa o comando para o algoritimo interpretar
            frase = microfone.recognize_google(audio,language = "pt-BR")
            
            self.falar(f" Mister o senhor disse {frase} ")
            print(f'{frase}')
            
            if "navegador" in frase:
                os.system("start Chrome.exe")
                self.falar("Abrindo o google,mais alguma coisa ?")
            
            elif "Gamer" in frase :
                self.falar("senhor qual jogo você deja jogar agora")
                try:
                    self.ouvir_microfone()
                    frase = microfone.recognize_google(audio,language = "pt-BR")
                    
                    if "Valorant" in frase :
                        py.press("win")
                        py.write("valorant")
                        py.press("enter")
                    elif"Cs" in frase:
                        pass
                    elif "Gta" in frase:
                            try:
                                # Caminho da pasta e do aplicativo
                                caminho_pasta = r'C:\Users\Home\Desktop\DIO'
                                caminho_aplicativo = os.path.join(caminho_pasta, 'Cherax.exe')
                                
                                # Abre a pasta (Opcional)
                                os.startfile(caminho_pasta)
                                time.sleep(2)  # Espera a pasta abrir

                               # Abre o aplicativo
                                py.doubleClick(x=365 , y =596)
                                time.sleep(1)
                                #clica no botao login
                                py.click(x=551,y=497)
                                time.sleep(3)
                                #leva o cursor e depois clica para iniciar
                                py.click(x=220,y=358)
                                py.doubleClick(x=220, y=358)
                                time.sleep(3)
                                # aceita o termo de segurança
                                time.sleep(5)
                                py.click(x=815, y=791)
                                py.click(x=927 , y=346)
                            except Exception as e:
                                print(f"Erro ao abrir o aplicativo: {e}")
                except sr.UnknownValueError:
                    print("Não entendi mestre")
                    return False
            elif "PowerPoint" in frase:
                os.system("start POWERPNT.exe")
                self.falar("Abrindo o google,mais alguma coisa ?")
            
            elif "trade" in frase :
                os.system(f'start "" "C:\\Users\Home\\AppData\\Roaming\\Nelogica\\Profit\\profitchart.exe"')
                self.falar("Abrindo o google,mais alguma coisa ?")
            
            elif  "fechar" in frase:
                os.system("exit")
                self.falar("Encerrando o assistente. Até logo, mestre!")
                return True
        
        except sr.UnknownValueError:
            print("Não entendi mestre")
            return False


if __name__ == "__main__":
    assistente = Assistent()
    while True:
        audio, microfone = assistente.ouvir_microfone()
        if assistente.tarefas(audio, microfone):
            break