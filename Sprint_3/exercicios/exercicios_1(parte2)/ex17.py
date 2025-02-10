lista_1 = []
lista_2 = []
lista_3 = []
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def dividir_lista(lista):
    if len(lista)%3 == 0:
        for posi,num in enumerate(lista):
            if posi < (len(lista)/3)*1:
                lista_1.append(num)
            elif posi < (len(lista)/3)*2:
                lista_2.append(num)
            else:
                lista_3.append(num)
        print(lista_1,lista_2,lista_3)
        
dividir_lista(valores)