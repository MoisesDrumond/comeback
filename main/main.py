from console_functions import default_question, option_not_found
# from crud_functions import create_user
import crud_functions

add_option = 1
list_option = 2
update_option = 3
delete_option = 4
exit_option = 5


def main():
    users = []
    option = None

    while option != exit_option:
        option = default_question()
        if option == add_option:
            crud_functions.create_user(users)

        elif option == list_option:
            crud_functions.list_user(users)

        elif option == update_option:
            crud_functions.update_user(users)
        
        elif option == delete_option:
            crud_functions.delete_user(users)

        elif option == exit_option:
            crud_functions.option_exit()

        else:
            option_not_found()

if __name__ == "__main__":
    main()
