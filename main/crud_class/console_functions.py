from os import system

def clear():
    system('clear')  # ou 'cls' no Windows

def default_question():
    return int(input(
        '1. Create user\n'
        '2. List users\n'
        '3. Update user\n'
        '4. Delete user\n'
        '5. Exit\n'
        'Choose an option: '
    ))

def option_not_found():
    try:
        clear()
        raise Exception('Opção não encontrada!')
    except Exception as error:
        clear()
        print(f'Erro: {error}')
