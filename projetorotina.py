import sys
from lib import main
import time

if __name__ == '__main__':
    print('###########################')
    print('Bem vindo ao projeto rotina')
    print('###########################')
    print('O projeto irá ser realizado dentro do DreamCraft com o objetivo de obter '
          'o máximo de lucro possível para o usuário. \nQuando quiser começar, digite \'start\'.\n')

    print('Atualmente temos: \n*Farm de Blaze Rod \n*Farm de Cacto (revenda) em 2 lojas.')

    while True:
        user_input = input('')
        if user_input.lower() == 'start':
            break
        elif user_input.lower() == 'exit':
            print('Saindo do sistema.')
            sys.exit(0)

    time.sleep(3)
    main.execute_farms()
    print('A rotina finalizou, aproveite seu money :) veja o quanto ganhou usando /money.')
