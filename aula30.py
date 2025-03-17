perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0  # Contador de acertos

for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}\n')

    # Mostrando as opções numeradas corretamente
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f'{i}) {opcao}')

    escolha = input('Escolha uma opção: ')

    # Pegando o índice da resposta correta
    indice_correto = pergunta["Opções"].index(pergunta["Resposta"])

    # Verificando se a escolha é correta
    if escolha.isdigit() and int(escolha) == indice_correto:
        print('✅ Acertou, miseravi!\n')
        acertos += 1  # Incrementa acerto
    else:
        print('❌ Tu errou, cria!\n')

# Exibir resultado final
print(f'Você acertou {acertos} de {len(perguntas)} perguntas!')
