class Ordenadora:
    def __init__(self,lista):
        self.listaBaguncada = lista
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)
    
    
crescente = Ordenadora([1, 2, 3, 4, 5])
decrescente = Ordenadora([9, 8, 7, 6])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())