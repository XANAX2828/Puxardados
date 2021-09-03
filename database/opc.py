import os, sys, time

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


error = f'{Twhite}[{Ired}ERROR{Twhite}]';
warning = f'{Twhite}[{Nyellow}!{Twhite}]';
info = f'{Twhite}[{Dgreen}i{Twhite}]'
result = os.popen('figlet MID-PAINEL').read()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    clear()
    print(f'''
{result}
-- P  A  I  N  E  L --
{info} Panel inspired by Kiny's / Coded by DR MIDNIGHT {info}
{warning} Este painel foi disponibilizado gratuitamente. Se pagou por isso, foi enganado. {warning}
       ''')


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def dialog(text='', tiled='='):
    clear();
    banner()
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    for txt in text:
        print(str(warning) + ' ' + txt)
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    time.sleep(3)


def menu(text='Sem Itens para mostrar.\nModo de teste', msg='Digite o numero da opção que deseja.', tiled='='):
    clear();
    banner()
    text = text.split('\n')
    number = 0
    for txt in text:
        number = number + 1
        if '::' in txt:
            riped = txt.split('::')
            print(str(Twhite) + '[' + str(Dgreen) + str(number) + str(Twhite) + '] ' + riped[0])
            print()
            number = number + 1
            print(str(Twhite) + '[' + str(Dgreen) + str(number) + str(Twhite) + '] ' + riped[1])
        else:
            print(str(Twhite) + '[' + str(Dgreen) + str(number) + str(Twhite) + '] ' + txt)
    print(info + ' ' + msg)
    return input('===>')


def dialog_choice(text='', msg='Deseja realizar uma nova consulta?', tiled='='):
    clear();
    banner()
    text = text.split('\n');
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    if maior > 2:
        print(tiled + tiled * maior + tiled + tiled)
        for txt in text:
            print(txt)
        print(tiled + tiled * maior + tiled + tiled)
    print(info + ' ' + msg)
    print(str(Twhite) + '[' + str(Dgreen) + str(1) + str(Twhite) + ']' + ' Sim')
    print(str(Twhite) + '[' + str(Dgreen) + str(2) + str(Twhite) + ']' + ' Não')
    return input('===>')


def input_dialog(text='', tiled='='):
    clear();
    banner()
    text = text.split('\n');
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    if maior > 2:
        msg = text[0]
    else:
        msg = 'Digite o número ou nome que deseja consultar.'
    print(info + ' ' + msg)
    return input('===>')


def error_dialog(text='', tiled='='):
    clear();
    banner()
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    for txt in text:
        print(str(error) + ' ' + txt + ' ' + str(error))
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    time.sleep(3)
