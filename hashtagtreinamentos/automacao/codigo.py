'''
Passo 1: Abrir o sistema da empresa;
Passo 2: fazer login;
    URL SISTEMA: https://dlp.hashtagtreinamentos.com/python/intensivao/login    
Passo 3: importar a base de dados dos produtos;
Passo 4: Cadastrar 1 produto;
Passo 5: Repetir o passo 4 até acabar todos os produtos;
'''

#para a automação usar o  pyautogui (instalar a extensão no terminal: pip install pyautogui)
import pyautogui
import time
#para definir o intervalo entre cada comando
pyautogui.PAUSE = 0.5

#Passo 1
'''
press -> pressioar uma tela
click -> clicar
wrie -> escrever
'''
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Pedir para o computador esperar 3 segundos
time.sleep(3) #usei o time pois o pause pyautogui redefiniria o intervalo entres os próximos comandos 
#Passo 2
pyautogui.click(x=818, y=415)
pyautogui.write("bia.c.menezes@hotmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha123")
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3
import pandas #pip install pandas openpyxl

dados = pandas.read_csv("produtos.csv")
print(dados)

#Passo 4
'''pyautogui.click(x=849, y=293)
#codigo produto
pyautogui.write("MOLO000251")
pyautogui.press("tab")
#marca
pyautogui.write("Logitech")
pyautogui.press("tab")
#tipo
pyautogui.write("Mouse")
pyautogui.press("tab")
#categoria
pyautogui.write("1")
pyautogui.press("tab")
#preco_unitario
pyautogui.write("25.95")
pyautogui.press("tab")
#custo
pyautogui.write("6.50")
pyautogui.press("tab")
#obs
pyautogui.write(" ")
pyautogui.press("tab")
#enviar o cadastro
pyautogui.press("enter")

#pyautogui.scroll(10000) #numero  positivo scroll pra cima e numero negativo scroll pra baixo
pyautogui.press("PageUp")'''

#Passo 5
#Laço de repetição para cadastrar cada linha do arquivo csv qu
#puxando cada campo atraves do nome da tabela no csv
for linha in dados.index:
    pyautogui.click(x=849, y=293) 
    #codigo produto
    codigo = dados.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = dados.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")    
    #tipo
    tipo = str(dados.loc[linha, "tipo"])
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria 
    categoria = dados.loc[linha, "categoria"]    
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = dados.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo 
    custo = dados.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    obs = str(dados.loc[linha , "obs"])
    #condição para registrar observação apenas se tiver algum texto no csv
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    #enviar o cadastro
    pyautogui.press("enter")
    #pyautogui.scroll(10000) #numero  positivo scroll pra cima e numero negativo scroll pra baixo
    pyautogui.press("PageUp")