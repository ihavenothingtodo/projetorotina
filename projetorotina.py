import sys

if __name__ == '__main__':
    print('###########################')
    print('Bem vindo ao projeto rotina')
    print('###########################')
    print('O projeto irá ser realizado dentro do DreamCraft com o objetivo de obter '
          'o máximo de lucro possível para o usuário. \nQuando quiser começar, digite \'start\'.\n')

    print('Atualmente temos: \n*Farm de Blaze Rod \n*Farm de Cacto (revenda) em 2 lojas.')

    if len(sys.argv) > 1 and sys.argv[1] != 'start':
        while True:
            user_input = input('')
            if user_input.lower() == 'start':
                break
            elif user_input.lower() == 'exit':
                print('Saindo do sistema.')
                sys.exit(0)
