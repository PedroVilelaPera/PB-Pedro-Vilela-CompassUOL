def calcular(calc):
    result = eval(f'{calc[1][0]}{calc[0]}{calc[1][1]}')
    return result

def calcular_valor_maximo(operadores,operandos):
    resultados = []
    calculos = list(zip(operadores,operandos))

    resultados = list(map(calcular, calculos))
    return max(resultados)
