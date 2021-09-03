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
    print('########## ### Consulta CEP ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cep_input = input(f'\n{Hcyan}Digite o CEP para consulta: ').strip()
            if len(cep_input) != 8:
                print(f'{Ired}!!! {Nyellow}CEP Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
        rjson = request.json()
        if 'erro' in rjson:
            restart = str(input(
                f'{Ired}==> CEP NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CEP ENCONTRADO <=={Nyellow} '))
            print(f'\nCEP             >>> {rjson["cep"]}')
            print(f'Logradouro      >>> {rjson["logradouro"]}')
            print(f'Complemento     >>> {rjson["complemento"]}')
            print(f'Bairro          >>> {rjson["bairro"]}')
            print(f'Cidade          >>> {rjson["localidade"]}')
            print(f'Estado          >>> {rjson["uf"]}')
            print(f'População[IBGE] >>> {rjson["ibge"]}')
            print(f'DDD             >>> {rjson["ddd"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
