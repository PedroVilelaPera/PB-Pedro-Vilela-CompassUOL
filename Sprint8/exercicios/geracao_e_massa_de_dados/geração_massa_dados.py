import random
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_random = 10000000

nomes_unicos = []

for x in range(0,qtd_nomes_unicos):
    nomes_unicos.append(names.get_full_name())

print('Gerando {} nomes aleatórios'.format(qtd_nomes_random))

nomes_selecionados = []

for x in range(0,qtd_nomes_random):
    nomes_selecionados.append(random.choice(nomes_unicos))

with open('geracao_e_massa_de_dados/nomes_aleatorios.txt', mode='w', encoding='utf-8') as arquivo:
    for nome in nomes_selecionados:
        arquivo.write(nome + '\n')
