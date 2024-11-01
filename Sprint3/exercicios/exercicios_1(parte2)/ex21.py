class Passaro:
    def __init__(self,nome,som):
        self.nome = nome 
        self.som = som
    def voar(self):
        print(self.nome)
        print('Voando...')

    def emitirsom(self):
        print(f'{self.nome} emitindo som...')
        print(f'{self.som} {self.som}')
        
        
    
class Pato(Passaro):
    def __init__(self):
        super().__init__('Pato', 'Quack')

class Pardal(Passaro):
    def __init__(self):
        super().__init__('Pardal', 'Piu')

pato = Pato()  
pardal = Pardal()
pato.voar()
pato.emitirsom()
pardal.voar()
pardal.emitirsom()

