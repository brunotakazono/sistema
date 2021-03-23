import sqlite3
from time import sleep
import os


conn = sqlite3.connect('sistemas.db')
cursor = conn.cursor()

nomeFantasia = input('nomeFantasia:')
razaoSocial = input('razaoSocial:')
CNPJ_1 = input("CNPJ: ")
for CNPJ in CNPJ_1:
    if len(CNPJ_1) >= 14:
        print("CNPJ INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        CNPJ_1 = CNPJ_1.zfill(14)
cnpj = '{}.{}.{}/{}-{}'.format(CNPJ_1[:2], CNPJ_1[2:5], CNPJ_1[5:8], CNPJ_1[8:12], CNPJ_1[12:])
inscEstadual = input('inscEstadual:')
telefone_1 = input('telefone:')
for telefone in telefone_1:
    if len(telefone_1) >= 8:
        print("TELEFONE INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        telefone_1 = telefone_1.zfill(8)
telefone = '{}-{}'.format(telefone_1[:4], telefone_1[4:])
email = input('email:')
site = input('site:')
obs = input('obs:')
cep_1 = input('cep:')
for cep in cep_1:
    if len(cep_1) < 14:
        print("CEP INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        cep_1 = cep_1.zfill(8)
cep = '{}.{}-{}'.format(cep_1[:2], cep_1[2:5], cep_1[5:])
endereco = input('endereco:')
numero = input('numero:')
bairro = input('bairro:')
cidade = input('cidade:')
estado = input('estado:')

for nome_fantasia in 'nomeFantasia':
    cursor.execute("SELECT count(*) FROM fornecedores WHERE nome_fantasia = ?", (nomeFantasia,))
    data = cursor.fetchone()[0]
if data == 0:
    cursor.execute('''
    INSERT INTO fornecedores (nome_fantasia,razao_social, cnpj, insc_estadual, telefone, email, site,
    obs, cep, endereco, numero, bairro, cidade, estado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (nomeFantasia, razaoSocial, cnpj, inscEstadual, telefone, email, site, obs, cep, endereco, numero,
                    bairro, cidade, estado))
    conn.commit()

    print('Dados inseridos com sucesso.')
    conn.close()
else:
    print("Error: Fornecedor ja Cadastrado.\n")
    sleep(5)
