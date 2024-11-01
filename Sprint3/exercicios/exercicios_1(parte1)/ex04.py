for n in range(1,101):
    ehprimo = 0
    if n > 1:
        for x in range(1,n+1):
            if n % x == 0:
                ehprimo += 1
    if ehprimo == 2:
        print(n)