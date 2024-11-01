def separar_valores(dicionario,conjunto):
    for chave,valor in dicionario.items():
        conjunto.add(valor)
    print(list(conjunto))        

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
conjunto_speed = set()
separar_valores(speed,conjunto_speed)