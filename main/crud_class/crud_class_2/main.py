from console_functions import clear, default_question
from crud_classes import UserManager 
def main():
    clear()
    manager = UserManager()
    option = None
    while option != 5:
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
            manager.exit()
    
if __name__ == "__main__":
    main()
