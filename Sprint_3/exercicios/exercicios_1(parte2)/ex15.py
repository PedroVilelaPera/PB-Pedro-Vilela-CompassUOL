class Lampada:
    def __init__(self,estado_inicial=False):
        self.ligada = estado_inicial
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada
        
lampada = Lampada()
lampada.liga()
print(f'A lâmpada está ligada? {lampada.esta_ligada()}')
lampada.desliga()
print(f'A lâmpada ainda está ligada? {lampada.esta_ligada()}')
    