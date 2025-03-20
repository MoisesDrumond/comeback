from os import system
def default_question():
    return int(input(
        '1. create user\n'
        '2. list user\n'
        '3. update user\n'
        '4. delete user\n'
        '5. exit user\n'
        'Choose an option:'
    ))

def option_not_found():
    try:
        raise Exception('Opção não encontrada!')
    except Exception as error:
        print(f'Erro: {error}')

def clear():
    system('clear')
