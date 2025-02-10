class Aviao:
    def __init__ (self,modelo,velocidade_maxima,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "Azul"
        self.capacidade = capacidade
    def __str__ (self):
        return f'modelo {self.modelo}: velocidade máxima {self.velocidade_maxima} km/h: capacidade para {self.capacidade}: Cor {self.cor}'
        
lista_avioes = []
aviao1 = Aviao('BOIENG456',1500,400)
lista_avioes.append(aviao1)
aviao2 = Aviao('Embraer Praetor 600',863,14)
lista_avioes.append(aviao2)
aviao3 = Aviao('Antonov An-2',258,12)
lista_avioes.append(aviao3)

for aviao in lista_avioes:
    print(aviao)