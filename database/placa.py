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
    print(f'\n{Iblue}########## #################### ##########')
    print('######### ### Consulta PLACA ### #########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            placa_input = input(f'\n{Hcyan}Digite a Placa para consulta: ').strip()
            if len(placa_input) != 7:
                print(f'{Ired}!!! {Nyellow}Placa Inválida {Ired}!!!')
            else:
                break
        request = requests.get(f'https://apicarros.com/v1/consulta/{placa_input}/json')
        rjson = request.json()
        if 'erro' in rjson:
            restart = str(input(
                f'{Ired}==> PLACA NÃO ENCONTRADA <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print(rjson)
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> PLACA ENCONTRADA <=={Nyellow} '))
            print(f'\nPlaca           >>> {rjson["placa"]}')
            print(f'Ano             >>> {rjson["ano"]}')
            print(f'Ano do Modelo   >>> {rjson["anoModelo"]}')
            print(f'Chassi          >>> {rjson["chassi"]}')
            print(f'Cor             >>> {rjson["cor"]}')
            print(f'Data            >>> {rjson["data"]}')
            print(f'Marca           >>> {rjson["marca"]}')
            print(f'Modelo          >>> {rjson["modelo"]}')
            print(f'Município       >>> {rjson["municipio"]}')
            print(f'Situação        >>> {rjson["situacao"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
