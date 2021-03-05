#!/usr/bin/python3

import os, time, sys
os.system("sudo apt-get install python3-pip")
os.system("sudo pip3 install colorama")
from colorama import Fore,init
init()



RESET = Fore.RESET

def banner():
    os.system("clear" or "cls")
    print(Fore.CYAN+"""
 
██╗      █████╗ ███████╗██╗███╗   ██╗███████╗███████╗███████╗    ██╗███╗   ██╗    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██║     ██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝██╔════╝██╔════╝    ██║████╗  ██║    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
██║     ███████║  ███╔╝ ██║██╔██╗ ██║█████╗  ███████╗███████╗    ██║██╔██╗ ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██║     ██╔══██║ ███╔╝  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║    ██║██║╚██╗██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
███████╗██║  ██║███████╗██║██║ ╚████║███████╗███████║███████║    ██║██║ ╚████║    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝

                version : 1.0
                Coded By abolfazlkheiri
                @Abitej
    """+RESET)
 
banner()



# https://pypi.org/project/py-notifier/
# $ python3 -m pip install py-notifier




def input_number(text='>> ', class_='~'):
    text_in_input, address_in_input = text, class_
    text_input = f'''
\u001b[38;5;160m┌─[\33[0m\u001b[38;5;87m{text_in_input}\33[0m\u001b[38;5;160m]─[\33[0m\u001b[38;5;142m{address_in_input}\33[0m\u001b[38;5;160m]\33[0m
\u001b[38;5;160m└──╼\33[0m\u001b[38;5;190m $ \33[0m'''
    return text_input

def clear():
    os.system('clear')
    if os.name == "posix": os.system('clear')
    elif os.name in ["nt", "dos", "ce"]: os.system('cls')
    else: print('\n' * 100)


revers_code = {
    '1' : 'update',
    '2' : 'upgrade',
    '3' : 'access root',
    '4' : 'Running program',
    '5' : 'Network(ifconfig)',
    '6' : 'See system tasks',
    '7' : 'Shut down the system at a specified time(Example: The system shuts down in 20 to 20 minutes)',
    '8' : 'To make sure the package is installed or not',
    '9' : 'Example: site.com',
    '10' : 'system specification',
}


while True:
    for x in range(1,  len(revers_code)+1  ): print(f'{x}>   {revers_code.get(str(x))}')

    x_code = input(input_number('number code'))

    if x_code.lower() == 'exit': sys.exit()
    elif x_code.lower() == 'help': clear(), print('\u001b[38;5;33m\n\n\n|-------------------------------|\n| exit | restart | help |\n|-------------------------------|\u001b[0m\n\n')
    elif x_code.lower() == 'restart': os.execl(sys.executable, sys.executable, * sys.argv)

    elif x_code in revers_code : 


        if int(x_code) == 1:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("sudo apt update")

        elif int(x_code) == 2:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("sudo apt upgrade")

        elif int(x_code) == 3:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("sudo su")

        elif int(x_code) == 4:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("ps")

        elif int(x_code) == 5:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("ifconfig")

        elif int(x_code) == 6:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("pstree")

        elif int(x_code) == 7:
            try:
                clear()
                print('\n\n'+revers_code.get(x_code))
                input_int = int(input(input_number('add', int(x_code))))
            except :pass
            os.system("shutdown -r" + input_int)

        elif int(x_code) == 8:
            clear()
            print('\n\n'+revers_code.get(x_code))
            which_int = input("Name of the package you want to see installed or not:")
            os.system("which" + "\t" + which_int)

        elif int(x_code) == 9:
            clear()
            print('\n\n'+revers_code.get(x_code))
            input_str = input(input_number('ping', int(x_code)))
            os.system("ping " + input_str)

        elif int(x_code) == 10:
            clear()
            print('\n\n'+revers_code.get(x_code))
            os.system("uname -a")
            time.sleep(1)

    else: clear()
        




