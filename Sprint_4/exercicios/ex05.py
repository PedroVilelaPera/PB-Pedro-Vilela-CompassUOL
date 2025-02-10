import csv

with open("estudantes.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in sorted(reader):
        notas = sorted(list(map(lambda nota: int(nota), row[1:])), reverse=True)[:3]
        media = round(sum(notas)/ 3, 2)
        print(f'Nome: {row[0]} Notas: {notas} Média: {media}')