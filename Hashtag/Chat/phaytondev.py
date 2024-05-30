import flet as ft
#x.add(conteudo) = adiciona
#ft.ElevatedButton(txt,on_click = função) = um botao com uma função
def main(page):
    import flet as ft
    texto =ft.Text('Retzin')
    page.add(texto)
    
    chat = ft.Column()
    
    def compartilha_menssage(mensagem):
        print (mensagem)
        #adicionando mensagem na tela
        text_menssage =ft.Text(f"{mensagem}")
        chat.controls.append(text_menssage)
        page.update()
    
    page.pubsub.subscribe(compartilha_menssage)
    
    def enviar_menssage(event):
        print("enviar menssagem")
        page.pubsub.send_all(f"{name_user.value}: {campo_mensagem.value}")
        #limpando campo menssagem
        campo_mensagem.value = '' 
        page.update()

    campo_mensagem = ft.TextField(label = 'Digite sua menssagem',on_submit = enviar_menssage)
    enviar = ft.ElevatedButton("Enviar",on_click = enviar_menssage)
    linha_enviar = ft.Row([campo_mensagem, enviar])
    
    def entrar_chat(event):
        print('entrar no chat')
        #fecha popup
        popup.open = False
        #tirar o botão
        page.remove(botao_iniciar)
        #tira o titulo
        page.remove(texto)
        #cria chat
        page.add(chat)
        page.pubsub.send_all(f"{name_user.value} entrou no chat")
        #botão enviar
        #coloca campo de digitar
        page.add(linha_enviar)
        page.update()
    
    title_popup = ft.Text('Welcome to Retzin')
    name_user = ft.TextField(label = 'Escreva seu nome no chat')
    botton_enter=ft.ElevatedButton(text = 'Entrar no chat',on_click=entrar_chat)  
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title = title_popup,
        content = name_user,
        actions=[botton_enter],
    )
    
    def abrir_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()
    
    botao_iniciar=ft.ElevatedButton("Iniciar",on_click = abrir_popup)
    page.add(botao_iniciar)


ft.app(target=main,view = ft.WEB_BROWSER)#cria app ou site ,view vazio = app