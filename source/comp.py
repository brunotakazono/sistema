def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033 [31m[ERRO: pro favor, digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033 [31m[ERRO: Usuario preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n






def linha(tam=42):
    return '-' * tam


def cabeçalho (txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabeçalho('Cadastro')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc =leiaInt('Sua Opção: ')
    return opc

def submenu(lista):
    cabeçalho('Sistema Principal')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc =leiaInt('Sua Opção: ')
    return opc

def ssubmenu(lista):
    cabeçalho('Financeiro')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc =leiaInt('Sua Opção: ')
    return opc