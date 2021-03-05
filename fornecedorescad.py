import sqlite3
from time import sleep

conn = sqlite3.connect('sistemas.db')
cursor = conn.cursor()

nomeFantasia = input('nomeFantasia:')
razaoSocial = input('razaoSocial:')
cnpj = input('cnpj:')
inscEstadual = input('inscEstadual:')
telefone = input('telefone:')
email = input('email:')
site = input('site:')
obs = input('obs:')
cep = input('cep:')
endereco = input('endereco:')
numero = input('numero:')
bairro = input('bairro:')
cidade = input('cidade:')
estado= input('estado:')




for nome_fantasia in ('nomeFantasia'):
    cursor.execute("SELECT count(*) FROM fornecedores WHERE nome_fantasia = ?", (nomeFantasia,))
    data = cursor.fetchone()[0]
if data == 0:
    cursor.execute('''
    INSERT INTO fornecedores (nome_fantasia,razao_social, cnpj, insc_estadual, telefone, email, site,
    obs, cep, endereco, numero, bairro, cidade, estado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
    (nomeFantasia, razaoSocial, cnpj, inscEstadual, telefone, email, site, obs, cep, endereco, numero, bairro, cidade, estado))
    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

else:
    print("Error: Username already in use.\n")
    sleep(5)