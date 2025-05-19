# crud_classes.py
from time import sleep
from console_functions import clear

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

class UserManager(User):
    def __init__(self):
        self.users = []

    def create_user(self):
        clear()
        try:
            name = input("Print your name: ")
            age = int(input("Print your age: "))
            self.users.append(User(name, age))
            clear()
            print("User successfully created!")
        except ValueError:
            clear()
            print("Invalid input!")

    def list_users(self):
        clear()
        if not self.users:
            print("There are no users yet.")
        else:
            for idx, user in enumerate(self.users):
                print(f"id: {idx}, {user}")

    def update_user(self):
        clear()
        if not self.users:
            print("There are no users yet.")
            return

        self.list_users()
        try:
            idx = int(input("Print the user id you wanna update: "))
            if 0 <= idx < len(self.users):
                name = input("Print your new name: ")
                age = int(input("Print your new age: "))
                self.users[idx].update(name, age)
                clear()
                print("User successfully updated!")
            else:
                clear()
                print("Invalid ID!")
        except ValueError:
            clear()
            print("Invalid input!")

    def delete_user(self):
        clear()
        if not self.users:
            print("There are no users yet.")
            return

        self.list_users()
        try:
            idx = int(input("Print the user id you wanna delete: "))
            if 0 <= idx < len(self.users):
                deleted_user = self.users.pop(idx)
                clear()
                print(f"The user {deleted_user.name} is already deleted.")
            else:
                clear()
                print("Invalid ID!")
        except ValueError:
            clear()
            print("Invalid input!")

    def exit_program(self):
        clear()
        print("Turning off...")
        sleep(1)
        clear()
