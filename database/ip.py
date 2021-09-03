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
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('########## ### Consulta IP ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            ip_input = input(f'\n{Hcyan}Digite o IP para consulta: ').strip()
            if len(ip_input) != 13:
                print(f'{Ired}!!! {Nyellow}IP Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'http://ip-api.com/json/{ip_input}')
        rjson = request.json()

        if rjson['status'] == 'fail':
            restart = str(input(
                f'{Ired}==> IP NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> IP ENCONTRADO <=={Nyellow} '))
            print(f'\nQuery[IP]          >>> {rjson["query"]}')
            print(f'País               >>> {rjson["country"]}')
            print(f'Código             >>> {rjson["countryCode"]}')
            print(f'Região             >>> {rjson["regionName"]}')
            print(f'Cidade             >>> {rjson["city"]}')
            print(f'Zip Code           >>> {rjson["zip"]}')
            print(f'Latitude           >>> {rjson["lat"]}')
            print(f'Longitude          >>> {rjson["lon"]}')
            print(f'Fuso Horário       >>> {rjson["timezone"]}')
            print(f'Fornecedor de Rede >>> {rjson["isp"]}')
            print(f'Conexão Org        >>> {rjson["as"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
