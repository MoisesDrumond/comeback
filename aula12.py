import os

senha = 'sexo'
letras_acertadas = ''
numero_tentativas = 0

while True:
    tentativa = input('Digite uma letra:')
    numero_tentativas += 1

    if len(tentativa) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if tentativa in senha:
        letras_acertadas += tentativa

    palavra_formada = ''
    for letra_secreta in senha:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == senha:
        os.system('clear')
        print('Voce ganhou, parabéns.')
        print('A palavra era', senha)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        # para acabar com o ciclo depois de concluir eu tiraria esse reset de info e daria um break no final
