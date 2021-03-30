import sqlite3

conn = sqlite3.connect('sistemas.db')

cursor = conn.cursor()

Nome = input("Cliente:")

cursor.execute('''SELECT * FROM cliente WHERE nome = ?''', (Nome,))
resulted = cursor.fetchone()
if Nome == None:
    print("Cliente não econtrado !!")
else:
    print('(nome | sobrenome | cpf | rg | celular | telefone | email | obs | cep | endereco | numero | bairro | cidade | estado | ')
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(resulted)