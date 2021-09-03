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

os.system('clear')

print(f'Painel de Consultas simples by Dr Midnight')


def clear():
    os.system('cls')
    os.system('clear')
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
import os, sys, time, json, subprocess, platform

try:
    import requests, random, json, phonenumbers
except:
    install = input(
        f'{Twhite}{Dgreen}[i]{Twhite} Vejo que é sua primeira vez aqui,'
        f'\nDeseja instalar o software necessário?\n1-Sim\n2-Não\n_').strip().upper()[0]
    if install == 'S' or install == '1':
        os.system("apt install figlet -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests pytube phonenumbers')
        clear()
    else:
        print(f'Tente realizar a instalação manual... Adeus');
        exit()
    restart()


try:
    from database import cep
    from database import covid19
    from database import ip
    from database import placa
    from database import opc
except Exception as error:
    print(f'{Twhite}{Ired}[*]{Twhite} Erro: ' + error)
    exit()

requests = requests.Session();result = os.popen('figlet MID').read()

try:
    if __name__ == '__main__':
        opc.dialog('Buscando atualizações ...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            opc.dialog('Atualização instalada.\nReiniciando o painel.')
            restart()
        else:
            print(f'{Twhite}[{Nyellow}i{Twhite}] Nenhuma atualizacao disponivel.')
            time.sleep(2)
except:
    if os.path.exists('.git'):
        pass
    else:
        opc.error_dialog('Falta de repositório GIT local')

try:
    subprocess.check_output('apt update -y', shell=True)
    os.system("apt install figlet curl -y")
except:
    os.system("pacman -Sy figlet curl")

Sair = False
while (Sair == False):
    try:
        op = int(opc.menu(f'''
        1  >>> BUSCADOR DE CEP
        2  >>> CONSULTAR IP
        3  >>> MOSTRAR MEU IP
        4  >>> CONSULTA PLACA
        5  >>> CONSULTAR CPF [{Ired}OFF{VRCRM}]
        6  >>> COVID19
        99 >>> Atualizar
        00 >>> Sair'''))
    except:
        opc.error_dialog('Caracteres não reconhecidos');
        op = None
    opc.clear()

    if op == 1:
        cep.consultar()
    elif op == 2:
        ip.consultar()
    elif op == 3:
        ip.consultar('25d800a8b8e8b99d77c809567aa291b8', 1)  # mostrar IP
    elif op == 4:
        placa.consultar()
    # elif op == 5:
        # cpf.consultar()
    elif op == 6:
        covid19.consultar()  # nCOVID19
    elif op == 99:  # Atualizar painel
        os.popen('cd data && bash update.sh');
        opc.dialog('Reiniciando o painel...');
        opc.restart()
    elif op == 00:
        Sair = True
    elif op == None:
        pass
    else:
        opc.error_dialog('Opção incorreta')
