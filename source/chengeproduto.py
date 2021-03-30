import sqlite3

conn = sqlite3.connect("sistemas.db")
cursor = conn.cursor()


def modifyData():
    for qtde in 'produto':
        cursor.execute("SELECT qtde FROM produto WHERE qtde = ?", (qtde,))
    update = input("Deseja alterar a quantidade no estoque Sim/Não? :")
    if update == "Sim":
        newqtde = input("Alterando qtde produto:")
        cursor.execute("UPDATE produto SET qtde='?' WHERE qtde='?'", (newqtde, qtde))
        conn.commit


modifyData()
