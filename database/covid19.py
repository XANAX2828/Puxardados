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
    os.system('cls')
    os.system('clear')


clear()


def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('######## ### Consulta Covid19 ### ########')
    print('########## #################### ##########')

    restart = 'S'
    while restart == 'S':
        print(f'\n{Iblue}########## #################### ##########')
        print('######## ### Consulta Covid19 ### ########')
        print('########## #################### ##########')
        while True:
            covid_input = str(input(f'\n{Hcyan}Digite o UF para consulta (Ex: "SP"/"RJ"): ').strip().lower())
            if len(covid_input) != 2:
                print(f'{Ired}!!! {Nyellow}UF Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{covid_input}')
        rjson = request.json()
        if 'error' in rjson:
            restart = str(input(
                f'{Ired}==> REGIÃO NÃO ENCONTRADA <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> REGIÃO ENCONTRADA <=={Nyellow} '))
            print(f'\nEstado(UF)       >>> {rjson["state"]}')
            print(f'Casos            >>> {rjson["cases"]}')
            print(f'Mortes           >>> {rjson["deaths"]}')
            print(f'Suspeitas        >>> {rjson["suspects"]}')
            print(f'Recusados        >>> {rjson["refuses"]}')
            print(f'Data de consulta >>> {rjson["datetime"]}')
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
