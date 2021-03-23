import sqlite3

conn = sqlite3.connect('sistemas.db')

cursor = conn.cursor()

NomeFantasia = input("NomeFantasia:")

cursor.execute('''SELECT * FROM fornecedores WHERE nome_fantasia = ?''', (NomeFantasia,))
resulted = cursor.fetchone()
if NomeFantasia == None:
    print("Fornecedor não econtrado !!")
else:
    print('ID | nomeFantasia | razaoSocial | cnpj | inscEstadual |telefone | email | site | obs | cep | endereco | numero | bairro | cidade | estado')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    print(resulted)



