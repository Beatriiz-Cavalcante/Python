import pandas as pd

# Definição das larguras das colunas com base no padrão do arquivo
colunas_largura = [
    (0, 29), (37, 46), (62, 70), (82, 94), (107, 134), (146, 292), (295, 364), 
    (364, None)
]

# Nomes das colunas (ajuste conforme necessário)
nomes_colunas = [
    "c1", "c2", "c3", "C4", "c5", 
    "c6", "c7", "c8"
]

# Função para processar o arquivo de largura fixa
def processar_arquivo_ret(CN31015A):
    with open(CN31015A, "r", encoding="utf-8") as file:
        linhas = file.readlines()
    
    dados_processados = []
    
    for linha in linhas:
        dados = [linha[inicio:fim].strip() for inicio, fim in colunas_largura]
        dados_processados.append(dados)
    
    df = pd.DataFrame(dados_processados, columns=nomes_colunas)

    for linha in linhas[:5]:  # Testando nas primeiras 5 linhas
        print("Última coluna:", repr(linha[364:]))  # Mostra os dados sem remover espaços
    
    return df

# Executar a função no arquivo
df = processar_arquivo_ret("CN31015A.ret")

# Visualizar os dados
print(df.head())

# Salvar em CSV para facilitar a leitura
df.to_csv("arquivo_corrigido.csv", index=False, encoding="utf-8")




