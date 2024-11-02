#Importando funções criadas por mim
#A função "criar_matriz_atores", lê o arquivo "actors.csv" e o transforma em uma matriz.
from funcoes import criar_matriz_atores
#E a função "escrever_arquivo" escreve o que eu desejar em um arquivo específico
from funcoes import escrever_arquivo
#Fiz isso pois vou usar essas funções em todos as etapas, e assim me poupa tempo.

#Lê o arquivo "actors.csv" e o transforma em uma matriz.
atores = criar_matriz_atores()

media_receita_atores = {}
for numlinha, linha in enumerate(atores):
    if numlinha == 5:
        media_receita_atores[f'{linha[0]}{linha[1]}'] = float(linha[4])
    elif numlinha != 0 and numlinha != 5:
        media_receita_atores[linha[0]] = float(linha[3])

#Pega a chave com o maior valor no dicionário "num_de_filmes"
ator_max_receita = max(media_receita_atores, key=media_receita_atores.get)

#Escreve no arquivo "etapa-1.txt" um texto com as informações necessárias
escrever_arquivo('Sprint3/exercicios/exercicios_2/etapa-3.txt','etapa_3',f'O ator com a maior média de receita de bilheteria bruta por filme é o {ator_max_receita}.')

