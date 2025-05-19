from os import system

def clear():
    system('clear')

def default_question():
    while True:  # Usar um loop para repetir até que o usuário forneça uma entrada válida
        try:
            option = int(input(
                '[1] Create user\n'
                '[2] List users\n'
                '[3] Update user\n'
                '[4] Delete user\n'
                '[5] Exit\n'
                'Choose an option: '))
            if 1 <= option <= 5:  # Verifica se a opção está entre 1 e 5
                return option
            else:
                clear()
                print("Invalid option! Please choose a number between 1 and 5.")
        except ValueError:
            clear()
            print("Invalid input! Please enter a valid number.")

# def option_not_found():
#     try:
#         clear()
#         raise Exception('Option not found!')
#     except Exception as error:
#         clear()
#         print(f'Erro:{error}')
