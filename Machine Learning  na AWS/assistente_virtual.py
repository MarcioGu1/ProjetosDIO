"""
programa que ira reconhecer a voz do user
e realizar comando no sistema operaconal

"""

#importando bibliotecas
from selenium import *
import pyttsx3
import subprocess
import os 
import speech_recognition as sr
import time

class Assistent:
    def __init__(self):
        self.falar("Bom dia,sou Friday sua assistente e irei te atender hoje")

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
            
            elif "Excel" in frase :
                os.system("start Excel.exe")
                    
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