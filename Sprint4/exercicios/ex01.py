with open('number.txt', 'r') as arquivo:
    nums = []
    for linha in arquivo:
        valores = linha.strip()
        nums.append(int(valores))

sorted_nums_pares = sorted(list(filter(lambda num: num%2 == 0, nums)), reverse=True)

maiores_nums = list(map(lambda valor: valor if sorted_nums_pares.index(valor) <= 4 else None, sorted_nums_pares))

maiores_nums = maiores_nums[0:5]

print(maiores_nums)
print(sum(maiores_nums))