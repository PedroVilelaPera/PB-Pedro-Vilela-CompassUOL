#Importando funções criadas por mim
#A função "criar_matriz_atores", lê o arquivo "actors.csv" e o transforma em uma matriz.
from funcoes import criar_matriz_atores
#E a função "escrever_arquivo" escreve o que eu desejar em um arquivo específico

#Lê o arquivo "actors.csv" e o transforma em uma matriz.
atores = criar_matriz_atores()

top1_filmes = []

for numlinha, linha in enumerate(atores):
    if numlinha == 5:
        top1_filmes.append(linha[5])
    elif numlinha != 0 and numlinha != 5:
        top1_filmes.append(linha[4])

aparicoes = dict.fromkeys(set(top1_filmes),0)

for chave,valor in aparicoes.items():
    for filme in top1_filmes:
        if filme == chave:
            aparicoes[chave] += 1

aparicoes = dict(sorted(aparicoes.items(), key=lambda item: item[1], reverse=True))

with open('Sprint3\exercicios\exercicios_2\etapa-4.txt', 'w', encoding='utf-8') as etapa_4:    
    for seq, (chave, valor) in enumerate(aparicoes.items()):
        etapa_4.write(f"{seq+1} - O filme {chave} aparece {valor} vez(es) no arquivo\n")

