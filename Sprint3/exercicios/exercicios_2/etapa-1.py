#Lê o arquivo "actors.csv" e o transforma em uma matriz.
with open('Sprint3/exercicios/exercicios_2/actors.csv', 'r') as arquivo:
    atores = []
    for linha in arquivo:
        linha = linha.strip()
        valores = linha.split(',')
        atores.append(valores)

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
with open('Sprint3/exercicios/exercicios_2/etapa-1.txt', 'w', encoding='utf-8') as etapa_1:    
    etapa_1.write(f'O ator com mais filmes é o {ator_max_filmes}, com {num_de_filmes[ator_max_filmes]} filmes.')
