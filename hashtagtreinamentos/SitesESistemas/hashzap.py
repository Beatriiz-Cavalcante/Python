#Descrição do projeto

# Titulo Hashzap
# botao de "iniciar chat"
    # popup para entrar no chat
        #Titulo "Bem vindo ao Haszap"
        #Campo de input com  placeholder "Digite o seu nome"
        #Botão "Entrar no chat"
#popup fecha
# quando entrar no chat: (aparece para todo mundo, inclusive para você) mensagem que fulano entrou no chat
#Campo de input com o placeholder "Digite aqui sua mensagem"
#Botão "enviar mensagem"
# a cada mensagem que você envia aparece para todo mundo nesse formato -> Nome: Texto da Mensagem

#importar o flet (no terminal -> pip install flet)
import flet as ft

#Criar uma função principal para rodar o aplicativo
def main(pagina):
    #titulo (elemento 1)
    titulo = ft.Text("Hashzap")
    #Estilo do chat (vertical)
    chat = ft.Column()

    #tunel de comunicação com o webscket (elemento 6 - não visual)
    def enviar_mensagem_tunel(mensagem):
        #função que vai ser executada por todos os usuários quando a mensaem for adicionada
        texto = ft.Text(mensagem) #define o ft.Text aqui porque quando convertido antes ficar mais complexo de passar pelo túnel 
        chat.controls.append(texto)
        pagina.update()
    #função para definir ações do tunel (a função usada pelo botao deve ser definida antes de ser chamada)
    #pubsub é a palavra reservada no flet para tunel de comunicação 
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    #função botaopopup (a função usada pelo botao deve ser definida antes de ser chamada)
    def entrar_chat(evento):
        #fechar popup
        popup.open = False
        #tirar título da tela
        pagina.remove(titulo)
        #tirar o botao inicial
        pagina.remove(botao)
        #Adicionar a definição do layout do chat
        pagina.add(chat)
        #carregar o chat (elemento 4)
        #input mensagem (elemento 4.1) 
        campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
        #carregar o campo enviar mensagem (elemento 5)
        def enviar_mensagem(evento):
            nome_usuario = caixa_nome.value
            texto_campo_mensagem = campo_enviar_mensagem.value
            mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
            pagina.pubsub.send_all(mensagem)
            #limpar a caixa de enviar mensagem
            campo_enviar_mensagem.value = ""
            pagina.update()
        #a função usada pelo botao deve ser definida antes de ser chamada
        #botão enviar mensagem (elemento 4.2)
        botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
        #aplicando o estilo (botar input e botão lado a lado)
        linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
         #estilo do chat
        pagina.add(linha_enviar)
        #adicionar no chat a mensagem "Fulano entrou no site"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
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
ft.app(main, view=ft.WEB_BROWSER) #para exibir no navegador é preciso enviar o parâmentro web browser na view, o padrão é o sistema desktop
#ft.app(main)