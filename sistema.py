from time import sleep
from comp import menu



while True:
    resposta = menu(['Cadastro', 'login', 'Sair'])
    if resposta == 1:
        while True:
            k = input('Deseja continuar? Sim/Não: ')

            if k == 'Sim':
                import db

                db.p_usuario
                db.p_senha
                db.p_email

                sleep(2)
                break
            if k == 'Não':
                sleep(2)
                break

    elif resposta == 2:
        import login
        login.user
        login.pswd
        while True:
            submenu = menu(['Cadastro de Produtos', 'Cadastro de Fornecedores', 'Consulta de Produtos', 'Consulta de Fornecedores', 'Voltar'])
            if submenu == 1:
                print('Aguarde')
            elif submenu ==2:
                print('Aguarde')
            elif submenu == 3:
                print('Aguarde')
            elif submenu == 4:
                print('Aguarde')
            elif submenu == 5:
                return resposta

    elif resposta == 3:
        print('saindo do sistema até logo.')
        break
    else:
        print('\033[31mERRO: Você digitou uma opção invalida \033[m')
        sleep(2)
