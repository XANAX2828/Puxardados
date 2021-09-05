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
def consulta():
   if os.geteuid() != 0:                # If not root user...
      os.system(f'{Twhite}Você {Ired}NÃO POSSUI {Twhite}privilégios ROOT')
   
   elif os.geteuid() == 0:              # If you are root user...
      os.system(f'{Twhite}Você {Dgreen}POSSUI {Twhite}privilégios ROOT')
