plvrs = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for plvr in plvrs:
    inver = ""
    for posi in range(len(plvr)-1,-1,-1):
        inver += plvr[posi]
    if plvr == inver:
        print(f'A palavra: {plvr} é um palíndromo')
    else:
        print(f'A palavra: {plvr} não é um palíndromo')

