"""
programa que ira reconhecer a voz do user
e realizar comando no sistema operaconal

"""

#importando bibliotecas

import pyautogui as py
import pyttsx3

import os 
import speech_recognition as sr
import time

class Assistent:
    def __init__(self):
        self.falar("Bom dia, senhorini")

    # Função para a assistente falar
    def falar(self, frase):
        engine = pyttsx3.init()
        engine.say(frase)
        engine.runAndWait()

    # Função para reconhecer a voz
    def ouvir_microfone(self):

        microfone = sr.Recognizer()


        with sr.Microphone() as source:


            microfone.adjust_for_ambient_noise(source)
            self.falar("Estou te ouvindo senhor, pode falar...")
            audio = microfone.listen(source)
            return audio, microfone

    # Função para processar tarefas
    def tarefas(self, audio, microfone):        
        try:
            frase = microfone.recognize_google(audio, language="pt-BR")
            self.falar(f"Mister, o senhor disse: {frase}")
            print(f'{frase}')

            if "navegador" in frase:
                self.abrir_navegador()

            elif "Gamer" in frase:
                self.abrir_jogo()

            elif "PowerPoint" in frase:
                os.system("start POWERPNT.exe")
                self.falar("Abrindo PowerPoint. Mais alguma coisa?")

            elif "trade" in frase:
                os.system(r'start "" "C:\\Users\\Home\\AppData\\Roaming\\Nelogica\\Profit\\profitchart.exe"')
                self.falar("Abrindo Profit. Mais alguma coisa?")

            elif "encerrar" in frase:
                self.falar("Encerrando o assistente. Até logo, mestre!")
                return True

        except sr.UnknownValueError:
            self.falar("Não entendi, mestre.")
            print("Não entendi, mestre")
            return False

    # Função para abrir o navegador e pesquisar
    def abrir_navegador(self):
        os.system("start Chrome.exe")
        time.sleep(2)
        self.falar("Abrindo o navegador. Deseja pesquisar algo?")
        audio, microfone = self.ouvir_microfone()
        frase = microfone.recognize_google(audio, language="pt-BR")
        if "sim" in frase:
            self.falar("Deseja pesquisar o que?")
            audio, microfone = self.ouvir_microfone()
            frase = microfone.recognize_google(audio, language="pt-BR")
            py.write(frase)
            py.press('enter')

    # Função para abrir jogos
    def abrir_jogo(self):
        self.falar("Qual jogo deseja jogar?")
        audio, microfone = self.ouvir_microfone()
        frase = microfone.recognize_google(audio, language="pt-BR")

        if "valorant" in frase:
            py.press("win")
            py.write("valorant")
            py.press("enter")
        elif "CS" in frase:
            # Coloque aqui o código para abrir CS
            pass
        elif "GTA" in frase:
            self.abrir_gta()

    # Função para abrir GTA com automações específicas
    def abrir_gta(self):
        try:
            caminho_pasta = r'C:\Users\Home\Desktop\DIO'
            caminho_aplicativo = os.path.join(caminho_pasta, 'Cherax.exe')
            os.startfile(caminho_pasta)
            time.sleep(2)

            py.doubleClick(x=365, y=596)
            time.sleep(1)
            py.click(x=551, y=497)
            time.sleep(3)
            py.click(x=220, y=358)
            py.doubleClick(x=220, y=358)
            time.sleep(3)
            time.sleep(5)
            py.click(x=815, y=791)
            py.click(x=927, y=346)
        except Exception as e:
            self.falar(f"Erro ao abrir o aplicativo: {e}")
            print(f"Erro ao abrir o aplicativo: {e}")


if __name__ == "__main__":
    assistente = Assistent()
    while True:
        audio, microfone = assistente.ouvir_microfone()
        if assistente.tarefas(audio, microfone):
            break