from time import sleep
from console_functions import clear

def create_user(users: list):
    clear()
    try:
        name = input('Print your name: ')
        age = int(input('Print your age: '))
        users.append({"name": name, "age": age})
        clear()
        print('User successfully created!')
    except ValueError:
        clear()
        print('Valor inválido')

def list_user(users: list):
    clear()
    if not users:
        print('There is no users yet.')
    for id, user in enumerate(users):
        print(f'id: {id}, name: {user['name']}, age: {user['age']}.')

def update_user(users: list):
    clear()
    if not users:
        clear()
        print('There is no users yet.')
        return
    list_user(users)
    try:
        update = int(input('Print the user id you wannna update: '))
        if 0 <= update < len(users):
            update_name = input('Print your new name: ')
            update_age = int(input('Print your new age: '))
            user = {'name': update_name, 'age': update_age}
            users[update].update(user)
            # users[update] = {'name': update_name, 'age': update_age}
            clear()
            print('User successfully updated!')
        else:
            clear()
            print('Valor inválido!')
        # 'nome': update_name, 'age': update_age
        # p1.update(nome='novo valor', idade=30)
    except ValueError:
        clear()
        print('Valor inválido!')

def delete_user(users: list):
    clear()
    if not users:
        clear()
        print('There is no users yet.')
    list_user(users)
    try:
        delete = int(input('Print the user id you wanna delete: '))
        if 0 <= delete < len(users):
            deleted = users.pop(delete)
            clear()
            print(f'The user {deleted['name']} is already deleted')
        else:
            clear()
            print('Valor inválido!')
    except ValueError:
        clear()
        print('Valor inválido!')

def option_exit():
    clear()
    print('Turning off...')
    sleep(1)
    clear()
