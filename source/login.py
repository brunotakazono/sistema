import sqlite3
import os

user = input("Usuario:")
pswd = input("Senha:")

db = sqlite3.connect('sistemas.db')
c = db.cursor()
c.execute('SELECT * from registro WHERE username="%s" AND senha="%s"' % (user, pswd))
data = c.fetchone()
if data is None:
    print("Login Failed !!")
    exec(open("login.py").read())
    os.system('cls' if os.name == 'nt' else 'clear')

else:
    print("Welcome")

c.close()
