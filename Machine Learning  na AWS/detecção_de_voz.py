"""
programa que ira reconhecer a voz do user
e realizar comando no sistema operaconal

"""

#importando bibliotecas

import os 
import speech_recognition as sr
import time

#Função para reconhecer a voz

def ouvir_microfone():
    #Habilita o microfone
    microfone = sr.Recognizer()

    #Usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritimo de redução de ruidos
        microfone.adjust_for_ambient_noise(source)

        print("Olá meu nome é malena sua assistente")
        time.sleep(1)
        print("Estou te ouvindo mestre pode falar...")

        #Armazena o comando em variavel
        audio = microfone.listen(source)
    
    try:
        
        #passa o comando para o algoritimo interpretar
        frase = microfone.recognize_google(audio,language = "pt-BR")

        print(f" Mestre o senhor disse {frase} ")

        if "navegador" in frase:
            os.system("start Chrome.exe")
            
        elif "Excel" in frase :
            os.system("start Excel.exe")
            
        elif "PowerPoint" in frase :
            os.system("start POWERPNT.exe")
            
        elif "Edge" in frase :
            os.system("start msedge.exe")
            
        elif  "fechar" in frase :
            os.system("exit")
            return True
    
    except sr.UnknownValueError:
        print("Não entendi mestre")
        return False
while True :
    if ouvir_microfone():
        break
