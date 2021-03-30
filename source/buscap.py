import sqlite3

conn = sqlite3.connect('sistemas.db')

cursor = conn.cursor()

Produto = input("Produto:")

cursor.execute('''SELECT * FROM produto WHERE produto = ?''', (Produto,))
resulted = cursor.fetchone()
if resulted == None:

    print("Produto não encontrado: ")
else:
    print('ID |produto | categoria | marca | estoqueMinimo | estoqueMaximo | qtdeProduto | valorCompra | valorUnitario |valorAtacado | qtdeAtacado | obsProduto')
    print('----------------------------------------------------------------------------------------------------------------------------------------------------')
    print(resulted)



