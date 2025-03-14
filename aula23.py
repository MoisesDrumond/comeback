def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par.'
    return f'{numero} é ímpar.'
print(impar_par(2))