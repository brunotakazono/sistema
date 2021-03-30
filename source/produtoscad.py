import sqlite3
from time import sleep

conn = sqlite3.connect('sistemas.db')
cursor = conn.cursor()

produto = input('produto:')
categoria = input('categoria:')
marca = input('marca:')
estoqueMinimo = input('estoqueMinimo:')
estoqueMaximo = input('estoqueMaximo:')
qtdeProduto = input('qtdeProduto:')
valorCompra = input('valorCompra:')
valorUnitario = input('valorUnitario:')
valorAtacado = input('valorAtacado:')
qtdeAtacado = input('qtdeAtacado:')
obsProduto = input('obsProduto:')

for produto in 'produto':
    cursor.execute("SELECT count(*) FROM produto WHERE produto = ?", (produto,))
    data = cursor.fetchone()[0]
if data == 0:
    cursor.execute('''
        INSERT INTO produto (produto,  categoria, marca, estoque_minimo, estoque_maximo, qtde,
        valor_compra, valor_unitario, valor_atacado, qtde_atacado, obs) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (produto,  categoria, marca, estoqueMinimo, estoqueMaximo, qtdeProduto, valorCompra,
                    valorUnitario, valorAtacado, qtdeAtacado, obsProduto))
    conn.commit()

    print('Dados inseridos com sucesso.')
    conn.close()
else:
    print("Error: Produto ja Cadastrado.\n")
    sleep(5)
