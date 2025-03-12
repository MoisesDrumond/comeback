import os
import sys

lista = []
while True:
    pergunta = input('[i]nserir [l]istar [a]pagar [s]air: ')
    os.system('clear')
    try:
        if pergunta.lower().startswith('i'):
            pergunta_1 = input('Digite seu nome: ')
            pergunta_2 = int(input('Digite sua idade: '))
            pergunta_3 = input('Digite sua descrição: ')
            lista.append([pergunta_1, pergunta_2, pergunta_3])
            os.system('clear')
            print('Regristrado com sucesso.')
    except ValueError:
        print('Digite um valor válido!')
    except Exception:
        print('erro desconhecido.')
    
    if pergunta.lower().startswith('l'):
        os.system('clear')
        for i, pessoa in enumerate(lista):
            print(f'id: {i}, nome: {pessoa[0]}, idade: {pessoa[1]}.')
        detalhes = input('Se quiser saber mais sobre uma pessoa, digite o id dela:\n'
                         'Se não quiser, digite [v]oltar: ')
        if detalhes.lower().startswith('v'):
            os.system('clear')
            continue
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
    
    if pergunta.lower().startswith('a'):
        if not lista:
            print('Nenhum usuário cadrastrado ainda.')
            continue
        for i, pessoa in enumerate(lista):
            print(f'id: {i}, nome: {pessoa[0]}, idade: {pessoa[1]}')
        deletar = int(input('Digite o ID do usuário a ser apagado: '))
        if 0 <= deletar < len(lista):
            deletado = lista.pop(deletar)
            print(f'Usuário {deletado[0]} deletado com sucesso.')
        else:
            print('ID Inválido')
        try:
            ...
        except ValueError:
            print('Este valor não é válido.')
        except Exception:
            print('Erro desconhecido.')
