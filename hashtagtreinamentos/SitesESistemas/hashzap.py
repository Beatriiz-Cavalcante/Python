# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

#importar o flet (no terminal -> pip indysll flet)
import flet as ft

#Criar uma função principal para rodar o aplicativo
def main(pagina):
    #titulo (elemento 1)
    titulo = ft.Text("Hashzap")

    chat = ft.Column()
        
    #função botaopopup
    def entrar_chat(evento):
        #fechar popup
        popup.open = False
        #tirar título da tela
        pagina.remove(titulo)
        #tirar o botao inicial
        pagina.remove(botao)
        #carregar o chat (elemento 4)
        campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
        #carregar o campo enviar mensagem (elemento 5)
        def enviar_mensagem(evento):
            nome_usuario = caixa_nome.value
            texto_campo_mensagem = campo_enviar_mensagem.value
            texto = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
            chat.controls.append(texto)
            #limpar a caixa de enviar mensagem
            campo_enviar_mensagem.value = ""
            pagina.update()
        #a função usada pelo botao deve ser definida antes de ser chamada
        botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
        #aplicando o estilo (botar input e botão lado a lado)
        linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
         #estilo do chat
        pagina.add(linha_enviar)
        #adicionar no chat a mensagem "Fulano entrou no site"
        nome_usuario = caixa_nome.value
        texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
        chat.controls.append(texto_mensagem)
        pagina.update()


    #popup (elemento 3)
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome") #textfield é como o input
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    #o que tem dentro do popup deve ser definido antes de ser usado
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    #botão inicial (elemento 2)
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    #a função usada pelo botao deve ser definida antes de ser chamada
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    

    #colocar elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)
    

#Executar essa função com o flet
#ft.app(main, view=ft.WEB_BROWSER) #para exibir no navegador é preciso enviar o parâmentro web browser na view, o padrão é o sistema desktop
ft.app(main)