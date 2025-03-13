import os
import sys

lista = []
while True:
    pergunta = input('[i]nserir [l]istar [a]pagar [s]air: ')
    try:
        if pergunta.lower() == 'i':
                os.system('clear')
                nome = input('Digite seu nome: ')
                idade = int(input('Digite sua idade: '))
                sobre = input('Digite sua descrição: ')
                lista.append([nome, idade, sobre])
                os.system('clear')

        elif pergunta.lower() == 'l':
            if not lista:
                os.system('clear')
                print('Não há usuário cadastrado.')
                continue
            for id, pessoa in enumerate(lista):
                print(f'id: {id}, nome: {pessoa[0]}, idade {pessoa[1]}.')
            detalhes = input(
                'Caso queira mais detalhes sobre determinada pessoa, digite seu id. '
                'Caso não queira, digite [v]oltar: '
            )
            if detalhes.lower() == 'v':
                os.system('clear')
                continue
            if 0 <= int(detalhes) < len(lista):
                os.system('clear')
                detalhes = int(detalhes)
                print(f'Descrição de {lista[detalhes][0]}: {lista[detalhes][2]}.')
            else:
                os.system('clear')
                print('Digite um id existente.')
                continue

        elif pergunta.lower() == 'a':
            if not lista:
                os.system('clear')
                print('Não há usuário cadastrado.')
                continue
            for id, pessoa in enumerate(lista):
                os.system('clear')
                print(f'id: {id}, nome: {pessoa[0]}, idade: {pessoa[1]}, sobre: {pessoa[2]}.')
            deletar = int(input('Digite o id do usuário a ser deletado: '))
            os.system('clear')
            if 0 <= deletar < len(lista):
                deletado = lista.pop(deletar)
                os.system('clear')
                print(f'O usuário {deletado[0]} de {deletado[1]} anos de idade foi deletado.')
            else:
                os.system('clear')
                print('O id de usuário digitado está incorreto.')

        elif pergunta.lower() == 's':
            os.system('clear')
            print('Saindo...')
            sys.exit()
            
        else:
            os.system('clear')
            print('Digite a função correta.')   
    except ValueError:
        os.system('clear')
        print('Você deveria digitar um número.')
    # except SystemExit:
    #     raise
    # except:
    #     if ValueError:
    #         os.system('clear')
    #         print('Você deveria digitar um número.')
    # except Exception as e:
    #     os.system('clear')
    #     print(f'Ocorreu um erro: {e}')
