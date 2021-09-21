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
    print(f'\n{Iblue}########## ##################### ##########')
    print('########## ### Consulta CNPJ ### ##########')
    print('########## ##################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cnpj_input = input(f'\n{Hcyan}Digite o CNPJ para consulta: ').strip()
            if len(cnpj_input) != 14:
                print(f'{Ired}!!! {Nyellow}CNPJ Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj_input}')
        rjson = request.json()
        if 'ERROR' in rjson['status']:
            restart = str(input(
                f'{Ired}==> CNPJ NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CNPJ ENCONTRADO <=={Nyellow} '))
            print('\nINFO:')
            print(f'CNPJ               >>> {rjson["cnpj"]}')
            print(f'Nome               >>> {rjson["nome"]}')
            print(f'Complemento        >>> {rjson["complemento"]}')
            print(f'Atividade Pri      >>> {rjson["atividade_principal"]}')
            print(f'Atividades Sec     >>> {rjson["atividades_secundarias"]}')
            print(f'Telefone           >>> {rjson["telefone"]}')
            print(f'Email              >>> {rjson["email"]}')

            print('\nLOCALIDADE:')
            print(f'Cep                >>> {rjson["cep"]}')
            print(f'Estado             >>> {rjson["municipio"]}{rjson["uf"]}')
            print(f'Bairro             >>> {rjson["bairro"]}')
            print(f'Logradouro         >>> {rjson["logradouro"]}{rjson["numero"]}')

            print('\nSITUAÇÃO')
            print(f'Situação           >>> {rjson["motivo_situacao"]}')
            print(f'Data Situação      >>> {rjson["data_situacao"]}')
            print(f'Situação Especial  >>> {rjson["situacao_especial"]}')
            print(f'Data               >>> {rjson["data_situacao_especial"]}')

            print('\nEXTRA')

            print(f'Última att         >>> {rjson["ultima_atualizacao"]}')
            print(f'Capital            >>> {rjson["capital_social"]}')
            print(f'Efr                >>> {rjson["efr"]}')
            print(f'Disponibilidade    >>> {rjson["billing"]}')

            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
