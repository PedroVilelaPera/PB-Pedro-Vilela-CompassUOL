#Importando funções criadas por mim
#A função "criar_matriz_atores", lê o arquivo "actors.csv" e o transforma em uma matriz.
from funcoes import criar_matriz_atores
#E a função "escrever_arquivo" escreve o que eu desejar em um arquivo específico
from funcoes import escrever_arquivo
#Fiz isso pois vou usar essas funções em todos as etapas, e assim me poupa tempo.

#Lê o arquivo "actors.csv" e o transforma em uma matriz.
atores = criar_matriz_atores()

#Criação da lista que armazenará as receitas brutas de todos os filmes.
receitas_brutas_filmes = []

#Adicionando os valores a lista "receitas_brutas_filmes".
for numlinha, linha in enumerate(atores):
    if numlinha == 5:
        #Aqui a posição da coluna na matriz está diferente pois há um erro de escrita no documento que não poderia ser alterado.
        #Com isso foi necessário realizar essa manobra.
        receitas_brutas_filmes.append(float(linha[6]))
    elif numlinha != 0 and numlinha != 5:
        receitas_brutas_filmes.append(float(linha[5]))

#Realiza a média dos valores da lista "receitas_brutas_filmes".
media_receitas = sum(receitas_brutas_filmes)/len(receitas_brutas_filmes)

#Escreve o valor da média no arquivo "etapa-2.txt"
escrever_arquivo('Sprint3/exercicios/exercicios_2/etapa-2.txt','etapa_2',f'A média das receitas de todos os filmes, considerando todos os atores, é de {media_receitas} milhões de dólares.')

