nome = input('Digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('seu nome é curto')
    if tamanho_nome >= 5 and tamanho_nome <= 6: # if tamanho_nome == 5 or tamanho_nome == 6:
        print('seu nome é normal')
    if tamanho_nome > 6:
        print('seu nome é grande')
else:
    print('Digite mais uma letra')
