from time import sleep
from console_functions import clear

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def update(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}.'
        
class UserManager():
    def __init__(self):
        self.users = []
        
    def create_user(self):
        clear()
        try:
            name = input('Print your name: ')
            age = int(input('Print your age: '))
            self.users.append(User(name, age))
            clear()
            print('User successfully created!')
        except ValueError as error:
            clear()
            print(error)
            print('Invalid input!')

    def list_users(self):
        if not self.users:
            clear()
            print('There is no user to list.')
            return
        else:
            for id, user in enumerate(self.users):
                clear()
                print(f'id:{id}, name: {user.name}, age: {user.age}.')
    
    def update_user(self):
        if not self.users:
            clear()
            print('There is no user to list.')
            return
        self.list_users()
        try:    
            id = int(input('Print the id to update: '))
            if 0 <= id < len(self.users):
                self.users[id].name = input('Print your name: ')
                self.users[id].age = int(input('Print your age: '))
                clear()
                print('User successfully updated!')
            else:
                clear()
                print('Invalid input!')
        except ValueError as error:
            clear()
            print(error)
            print('Invalid input!')
    
    def delete_user(self):
        if not self.users:
            clear()
            print('There is no user to list.')
            return
        self.list_users()
        try:
            id = int(input('Print the id to delete: '))
            deleted = self.users.pop(id)
            clear()
            print(f'User: {deleted.name} has been deleted.')
        except (ValueError, IndexError) as error:
            clear()
            print(error)
            print('Invalid input!')

    def exit(self):
        clear()
        print("Turning off...")
        sleep(1)
        clear()
