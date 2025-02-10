class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
        self.id = ''
    def nome(self):
        print(self.__nome)
        
pessoa = Pessoa('Fulano de Tal') 
pessoa.nome()