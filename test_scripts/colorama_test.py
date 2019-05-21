from colorama import Fore, init, Style


class urmom:
    def __init__(self):
        init()
        print(Fore.RED + 'some red text')
        print(Style.DIM + 'and in dim text' + Style.RESET_ALL)
        print('back to normal now')
        COLORNAME = 'RED'
        color = getattr(Fore, COLORNAME)
        print(color + "hi")


while True:
    return