numero = input('Digite um número inteiro:')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar: #já é True
        par_impar_texto = 'par'

    print(f'o número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

# try:
#     numero_int = float(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar: #já é True
#         par_impar_texto = 'par'

#     print(f'o número {numero_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')