import hashlib

string = input("Insira o texto que gostaria de codificar: ")

string_codificada = hashlib.sha1(string.encode()).hexdigest()

print(f'O texto "{string}" em hash é igual a: \n{string_codificada}')

