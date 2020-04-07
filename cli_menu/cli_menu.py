import sys
import os

# Menu definition are defined as 'menu_actions'-dicts, which is passed along to 'exec_menu'
# menu_actions has key-press as key and the function name to call as value.
# menu_actions = {
#     'main_menu': main_menu,
#     '1': menu1,
#     '2': menu2,
#     '7': hello1,
#     '8': hello2,
#     '9': back,
#     '0': exit,
# }

# In order to make sub-menus and functions return you to same menu places, I am using sys._getframe() to re-execute menu functions


def clear_screen():
    # for windows
    if os.name == 'nt':
        return os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        return os.system('clear')


def main_menu():
    menu_actions = {
        '1': menu1,
        '2': menu2,
        '7': hello1,
        '8': hello2,
        '9': back,
        '0': exit,
    }
    print("Welcome to the system!\n")
    print("Please choose the menu you want to start:")
    print("1. Menu 1")
    print("2. Menu 2")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice, menu_actions)


def exec_menu(choice, menu_actions):
    clear_screen()
    ch = choice.lower()
    if ch == '':
        main_menu()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            # TODO: Is this okay? It works, but it seems like a hack. :)
            globals()[sys._getframe().f_back.f_code.co_name]()


def menu1():
    menu_actions = {
        'main_menu': main_menu,
        '7': hello1,
        '9': back,
        '0': exit,
    }
    print("Hello Menu 1 !\n")
    print("7. Hello1")
    print("9. Back to Main")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice, menu_actions)


def menu2():
    menu_actions = {
        'main_menu': main_menu,
        '8': hello2,
        '9': back,
        '0': exit,
    }
    print("Hello Menu 2 !\n")
    print("8. Hello2")
    print("9. Back to Main")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice, menu_actions)


def back():
    main_menu()


def exit():
    sys.exit(0)


def back_to_menu():
    '''This goes back to the same menu as where you came from using a sys._getframe call.'''
    # TODO: Is this okay? It works, but it seems like a hack. :)
    globals()[sys._getframe(2).f_back.f_code.co_name]()


def hello1():
    print("Hello1")
    back_to_menu()


def hello2():
    print("Hello2")
    back_to_menu()


if __name__ == "__main__":
    clear_screen()
    main_menu()
