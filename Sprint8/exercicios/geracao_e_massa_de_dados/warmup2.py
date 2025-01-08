animais = ['Elefante','Golfinho','Arara','Canguru','Cobra','Pinguim','Leão','Jacaré','Girafa','Zebra','Urso-pardo','Lobo','Ornitorrinco','Tigre','Peixe-palhaço','Camaleão','Coruja','Tartaruga','Cavalo-marinho','Falcão-peregrino']

animais.sort()

with open('animais_ordenados.csv', mode='w', encoding='utf-8') as arquivo:
    arquivo.write('Animal\n')

    for animal in animais:
        arquivo.write(animal + '\n')
