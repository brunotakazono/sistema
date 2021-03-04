import sqlite3

conn = sqlite3.connect('Cadastro.db')


cursor = conn.cursor()


p_usuario = input('Usuario: ')
p_senha = input('Senha: ')
p_email = input('Email: ')

for username in ('p_usuario'):
    cursor.execute("SELECT count(*) FROM registro WHERE username = ?", (p_usuario,))
    data = cursor.fetchone()[0]
if data == 0:
    cursor.execute("""
    INSERT INTO registro (username, senha, email)
    VALUES (?,?,?)
    """, (p_usuario, p_senha, p_email))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()
else:
    print("Error: Username already in use.\n")