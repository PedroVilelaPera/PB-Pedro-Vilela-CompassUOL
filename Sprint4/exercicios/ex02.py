vogais = ['a','e','i','o','u']

def conta_vogais(texto:str)-> int:
    texto_minus = texto.lower()
    texto_vogais = list(filter(lambda letra: letra in vogais, texto_minus))
    return(len(texto_vogais))
      
