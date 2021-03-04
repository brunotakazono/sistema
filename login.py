import sqlite3

user = input("Usuario:")
pswd = input("Senha:")

db = sqlite3.connect('Cadastro.db')
c = db.cursor()
c.execute('SELECT * from registro WHERE username="%s" AND senha="%s"' % (user, pswd))
data = c.fetchone()
if data is None:
    print("Login Failed")

else:
    print("Welcome")

c.close()
