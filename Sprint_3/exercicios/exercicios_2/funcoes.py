def criar_matriz_atores():
    with open('Sprint3/exercicios/exercicios_2/actors.csv', 'r') as arquivo:
        atores = []
        for linha in arquivo:
            linha = linha.strip()
            valores = linha.split(',')
            atores.append(valores)
    return atores

#A função "criar_matriz_atores" resumidamente cria uma matriz(Lista de listas) que contem todas as linhas do arquivo "actors.csv".

def escrever_arquivo(caminho,nome_arquivo,texto):
    with open(caminho, 'w', encoding='utf-8') as nome_arquivo:    
        nome_arquivo.write(texto)

#A função "escrever_arquivo" me permite inserir uma mensagem no arquivo que desejar.

