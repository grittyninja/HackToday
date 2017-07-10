# Tested only in python 3

from speeto import speeto




def help():
    # help section for program usage & options
    print('Usage: main.py args')
    print('Args: blabla')




def start():  # interactive mode, including listener & client setup
    print('Hi lets get started from the beginning')

def bad_args():
    print('Bad Arguments')

def console(obj):
    while True:
        inp = input(">>> ")
        inp_splitted = str.split(inp)

        if inp == 'help':
            help()
        elif inp == 'start':
            start()
        elif inp == 'exit':
            exit()
        elif inp_splitted[0] == 'connect':
            if len(inp_splitted) != 3:
                bad_args()
                print('Example: connect 127.0.0.1 8989')
                continue

            try:
                PORT = int(inp_splitted[2])
            except:
                bad_args()
                continue

            HOST = inp_splitted[1]
            obj.connect_socket(HOST,PORT)

        elif inp_splitted[0] == 'listen':
            obj.create_socket()


def main():
    a = speeto()
    print('Welcome to Speeto console')
    print('Multiplatform speed test')
    print('')
    print('try to type "help" or "status"')
    print('type "start" for interactive mode')
    print('------------------------')

    console(a)


if __name__ == '__main__':
    main()
