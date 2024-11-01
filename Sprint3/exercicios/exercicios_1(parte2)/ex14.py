def imprimir_valores(*args,**kwargs):
    for arg in args:
        print(str(arg)) 
    for chave, valor in kwargs.items():
        print(str(valor)) 

imprimir_valores(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)