import os
import sys

lista = []

while True:
    pergunta = input('[i]nserir [l]istar [a]pagar [s]air: ')
    os.system('clear')
    if pergunta.lower().startswith('i'):
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        sobre = input('Digite a descrição: ')
        lista.append([nome, idade, sobre])
        os.system('clear')
        print('Usuário cadastrado com sucesso.')
    
    if pergunta.lower().startswith('l'):
        os.system('clear')
        if not lista:
            print('Ainda não há usuários cadastrados.')
            continue
        for id, pessoa in enumerate(lista):
            print(f'id: {id}, nome: {pessoa[0]}, idade: {pessoa[1]}.')
        detalhes = input('Para mais informações sobre alguém, digite o id desejado:\n'
                         'Caso queira, digite [v]oltar: ')
        if detalhes.lower().startswith('v'):
            os.system('clear')
            continue
        else:
            os.system('clear')
            detalhes = int(detalhes)
            print(f'Descrição de {lista[detalhes][0]}: {lista[detalhes][2]}.')
            
    if pergunta.lower().startswith('a'):
        if not lista:
            print('Nenhum usuário foi cadastrado ainda.')
            continue
        for id, pessoa in enumerate(lista):

            print(f'id: {id}, nome: {pessoa[0]}, idade: {pessoa[1]}.')
        deletar = int(input('Para apagar o usuário, digite seu id: '))
        deletado = lista.pop(deletar) # deletado = lista[deletar] na outra linha. del lista[deletar]
        os.system('clear')
        print(f'O usuário {deletado[0]} de {deletado[1]} anos de idade, foi deletado.')

    if pergunta.lower().startswith('s'):
        os.system('clear')
        print('Saindo...')
        sys.exit()
