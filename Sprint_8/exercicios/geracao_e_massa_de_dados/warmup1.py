import random

nums = []

for x in range(250):
    nums.append(random.randint(1,500))

nums.reverse()

print('[LISTA DE NÚMEROS ALEATÓRIOS REVERTIDOS]')
print(nums)