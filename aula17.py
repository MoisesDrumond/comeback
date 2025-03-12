import os

lista = []
while True:
    pergunta = input(
    'Selecione uma opção\n'
    '[i]nserir [a]pagar [l]istar:')

    if pergunta.lower().startswith('i'):
        os.system('clear')
        create = input('Valor desejado:')
        lista.append(create)

    elif pergunta.lower().startswith('a'):
        indice_str = input('Escolha o índice a ser apagado:')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número int.')
        except IndexError:
            print('índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')

    elif pergunta.lower().startswith('l'):
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar.')

        for indice, item in enumerate(lista):
            print(indice, item)
                
