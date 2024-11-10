from functools import reduce

def credit_ou_debit(lancamento):
    if lancamento[1] == 'C':
        return +lancamento[0]
    else:
        return -lancamento[0]
    
def calcula_saldo(lancamentos):
    credit_debit = list(map(credit_ou_debit, lancamentos))
    
    valor_final = reduce(lambda valor_final, num: valor_final + (num), credit_debit)

    return valor_final