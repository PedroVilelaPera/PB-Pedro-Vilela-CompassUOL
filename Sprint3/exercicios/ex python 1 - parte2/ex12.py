def potencia(num):
    total = num * num
    return total
    
def my_map(lista, potencia, results):
    for num in lista:
        result = potencia(num)
        results.append(result)
    return results
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = []

print(my_map(nums, potencia, results))