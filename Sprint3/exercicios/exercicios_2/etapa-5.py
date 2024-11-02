#Importando funções criadas por mim
#A função "criar_matriz_atores", lê o arquivo "actors.csv" e o transforma em uma matriz.
from funcoes import criar_matriz_atores
#Fiz isso pois vou usar essas funções em todos as etapas, e assim me poupa tempo.

#Lê o arquivo "actors.csv" e o transforma em uma matriz.
atores = criar_matriz_atores()

receita_atores = {}
for numlinha, linha in enumerate(atores):
    if numlinha == 5:
        receita_atores[f'{linha[0]}{linha[1]}'] = float(linha[2])
    elif numlinha != 0 and numlinha != 5:
        receita_atores[linha[0]] = float(linha[1])

receita_atores = dict(sorted(receita_atores.items(), key=lambda item: item[1], reverse=True))

#Escreve no arquivo "etapa-1.txt" um texto com as informações necessárias
with open('Sprint3\exercicios\exercicios_2\etapa-5.txt', 'w', encoding='utf-8') as etapa_5:    
    for chave, valor in receita_atores.items():
        etapa_5.write(f"{chave} - {valor}\n")

        