import os
import sys

lista = []
while True:
    pergunta = input(
    '[i]nserir [l]istar [a]pagar [s]air:')

    if pergunta.lower().startswith('i'):
        nome = input('Digite seu nome:')
        idade = int(input('Digite sua idade:'))
        sobre = input('Diga algo sobre você:')
        lista.append([nome, idade, sobre])
        os.system('clear')
        print('Informações guardadas!')

    elif pergunta.lower().startswith('l'):
        os.system('clear')
        for i, pessoa in enumerate(lista):
            print(f'id: {i}, nome: {pessoa[0]}, idade: {pessoa[1]}.')
        detalhes = input('Se quiser saber mais sobre uma pessoa, digite o id dela:\n'
                         'Se não quiser, digite [v]oltar: ')
        if detalhes.lower().startswith('v'):
            os.system('clear')
        try:
            detalhes = int(detalhes)
            if 0 <= detalhes < len(lista):
                os.system('clear')
                print(f'\nDescrição de {lista[detalhes][0]}: {lista[detalhes][2]}\n')
            else:
                os.system('clear')
                print("ID inválido!\n")
        except ValueError:
            os.system('clear')
            print("Digite um número válido!\n")

    elif pergunta.lower().startswith('a'):
        if not lista:
            print("Nenhum usuário cadastrado.\n")
            continue

        os.system('clear')
        print("\nLista de Pessoas:")
        for i, pessoa in enumerate(lista):
            print(f'ID: {i}, Nome: {pessoa[0]}, Idade: {pessoa[1]}.')

        try:
            deletar = int(input('Digite o ID do usuário que quer deletar: '))

            if 0 <= deletar < len(lista):
                deletado = lista.pop(deletar)
                print(f'Usuário {deletado[0]}, {deletado[1]} anos, foi deletado com sucesso!\n')
            else:
                print("ID inválido!\n")

        except ValueError:
            print("Digite um número válido!\n")
    
    elif pergunta.lower().startswith('s'):
        print("Saindo...")
        sys.exit()

    else:
        print("Opção inválida. Tente novamente.\n")
