from time import sleep
from comp import menu, submenu
import sys
import os

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
                os.system('cls' if os.name == 'nt' else 'clear')
                sleep(5)
                break
            if k == 'Não':
                sleep(5)
                break

    elif resposta == 2:
        import login

        login.user
        login.pswd
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(5)
        while True:
            mainmenu = submenu(
                ['Cadastro de Produtos', 'Cadastro de Fornecedores', 'Consulta de Produtos', 'Consulta de Fornecedores',
                 'Cadastro de Clientes', 'Consulta de Clientes', 'Voltar'])
            if mainmenu == 1:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Cadastro de Produtos')
                        exec(open("./produtoscad.py").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 2:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Cadastro de Fornecedores')
                        exec(open("./fornecedorescad.py", encoding="utf8").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 3:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Consulta de Produtos')
                        exec(open("buscap.py").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 4:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Consulta de Fornecedores')
                        exec(open("buscaf.py").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 5:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Cadastro de Clientes')
                        exec(open("cadcliente.py", encoding="utf8").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 6:
                while True:
                    k = input('Deseja continuar? Sim/Não: ')
                    if k == 'Sim':
                        print('Consulta de Cleintes')
                        exec(open("buscac.py").read())
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    if k == 'Não':
                        print("Retornando ao Menu")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sleep(2)
                        break
            elif mainmenu == 7:
                print('saindo do sistema até logo.')
                os.system('cls' if os.name == 'nt' else 'clear')
                break
    elif resposta == 3:
        print('saindo do sistema até logo.')
        sys.exit()
    else:
        print('\033[31mERRO: Você digitou uma opção invalida \033[m')
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(2)
