import hashlib

continuar = True

while continuar == True:
    print("[CODIFICADOR]")
    print("[1] Codificar")
    print("[0] Sair")
    
    acao = int(input("Insira o número correspondente a ação desejada: "))
    if acao == 1:
        string = input("\nInsira o texto que gostaria de codificar: ")

        string_codificada = hashlib.sha1(string.encode()).hexdigest()

        print(f'O texto "{string}" em hash é igual a: \n{string_codificada}\n')
    if acao == 0:
        continuar = False

