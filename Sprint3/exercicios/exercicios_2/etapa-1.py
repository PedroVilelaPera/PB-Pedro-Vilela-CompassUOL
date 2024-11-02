#Importando funções criadas por mim
#A função "criar_matriz_atores", lê o arquivo "actors.csv" e o transforma em uma matriz.
from funcoes import criar_matriz_atores
#E a função "escrever_arquivo" escreve o que eu desejar em um arquivo específico
from funcoes import escrever_arquivo
#Fiz isso pois vou usar essas funções em todos as etapas, e assim me poupa tempo.

#Lê o arquivo "actors.csv" e o transforma em uma matriz.
atores = criar_matriz_atores()

#Cria um dicionário chamado "num_de_filmes" com o nome dos atores e a quantidade de filmes que ele participou.
num_de_filmes = {}
for numlinha, linha in enumerate(atores):
    if numlinha == 5:
        #Trata a linha do ator Robert Downey Jr. que está com um problema em que ele separa o "jr" em outra coluna.
        #Aqui eu junto as duas colunas para que o nome dele fique correto e além disso troco a coluna de onde está sendo pego o valor do número de filmes.
        num_de_filmes[f'{linha[0]}{linha[1]}'] = int(linha[3])
    elif numlinha != 0 and numlinha != 5:
        num_de_filmes[linha[0]] = int(linha[2])

#Pega a chave com o maior valor no dicionário "num_de_filmes"
ator_max_filmes = max(num_de_filmes, key=num_de_filmes.get)

#Escreve no arquivo "etapa-1.txt" um texto com as informações necessárias
escrever_arquivo('Sprint3/exercicios/exercicios_2/etapa-1.txt','etapa_1',f'O ator com mais filmes é o {ator_max_filmes}, com {num_de_filmes[ator_max_filmes]} filmes.')