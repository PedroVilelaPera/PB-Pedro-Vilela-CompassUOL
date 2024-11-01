class Calculo:
    def __init__(self,X,Y):
        self.x = X
        self.y = Y
    def somar(self):
        soma = self.x+self.y
        print(f'Somando: {self.x}+{self.y} = {soma}')
    def subtrair(self):
        subtracao = self.x-self.y
        print(f'Subtraindo: {self.x}-{self.y} = {subtracao}')
        
calculo = Calculo(4,5)
calculo.somar()
calculo.subtrair()