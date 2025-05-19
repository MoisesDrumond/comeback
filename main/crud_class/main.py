# main.py
from console_functions import default_question, option_not_found, clear
from crud_classes import UserManager

def main():
    clear()
    option = None
    manager = UserManager()

    while option != 5:
        try:
            option = default_question()
            if option == 1:
                manager.create_user()
            elif option == 2:
                manager.list_users()
            elif option == 3:
                manager.update_user()
            elif option == 4:
                manager.delete_user()
            elif option == 5:
                manager.exit_program()
            else:
                option_not_found()
        except ValueError:
            clear()
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
