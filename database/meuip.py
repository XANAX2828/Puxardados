## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def consultar():
    clear()
    import netifaces
    gateways = netifaces.gateways()
    gateway_padrao = gateways['default'][netifaces.AF_INET][0]
    print(f"{Hcyan}Your computer's IP address is: \n{Nyellow}{gateway_padrao}")
    input('')
    clear()
