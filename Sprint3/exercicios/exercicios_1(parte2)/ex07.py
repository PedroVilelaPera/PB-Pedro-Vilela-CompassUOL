a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums_impar = []

for num in a:
    if num % 2 != 0:
        nums_impar.append(num)
        
print(nums_impar)
        