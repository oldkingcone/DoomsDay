try:
    from colorama import Fore, Back, Style, init
except ImportError as e:
    print(Fore.WHITE+Back.RED+"Docker Customize module failed: \n-> {}".format(e))
init(autoreset=True)
def docker_customize():
    x = 't'
    selection = str(input(Fore.WHITE+Back.ORANGE+"[ ?? ] Would you like to customize the docker container? [ ?? ] \n->")).lower()
    if selection == 'y':
        docker_file = open('./Dockerfile', 'w')
        while x == 't':
            stack = str(input(Fore.WHITE+Back.YELLOW+"[ ?? ] Which stack would you like to choose?\n"
                              "( 1 ) LAMP\n"
                              "( 2 ) MEAN\n"
                              "( 3 ) Original Setting[Installs Apache2 and Python3) [ ?? ]\n->"))
            if stack == 1:
                print(Fore.WHITE+Back.GREEN+"[*] Sticking with original OS, feel free to change this line,\n"
                      "FROM ubuntu:latest, to customize down to the OS of the container.")
                magic = open('./data/LAMP', 'r')
                mike = magic.readlines()
                magic.close()
                docker_file.writelines(''.join(mike))
                x = 'f'
            if stack == 2:
                print(Fore.WHITE+Back.GREEN+"[*] Sticking with original OS, feel free to change this line,\n"
                      "FROM ubuntu:latest, to customize down to the OS of the container.")
                magic = open('./data/MEAN', 'r')
                mike = magic.readlines()
                magic.close()
                docker_file.writelines(''.join(mike))
                x = 'f'
            if stack == 3:
                print(Fore.WHITE+Back.RED+"[**] No changes will be made to docker file, continuing! [**]")
                x = 'f'
