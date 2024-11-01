valores = "1,3,4,6,10,76"
lista_valores = valores.split(',')
soma = 0
for num in lista_valores:
    soma += int(num)
    
print(soma)