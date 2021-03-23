import sqlite3
from time import sleep
import os

conn = sqlite3.connect('sistemas.db')
cursor = conn.cursor()

nome = input("nome: ")
sobrenome = input("sobrenome: ")
cpf_1 = input("CPF: ")
for cpf in cpf_1:
    if len(cpf_1) >= 11:
        print("CPF INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        cpf_1 = cpf_1.zfill(11)
cpf = '{}.{}.{}-{}'.format(cpf_1[:3], cpf_1[3:6], cpf_1[6:9], cpf_1[9:])
rg_1 = input("RG: ")
for rg in rg_1:
    if len(rg_1) >= 11:
        print("RG INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        rg_1 = rg_1.zfill(9)
rg = '{}.{}.{}-{}'.format(rg_1[:2], cpf_1[2:5], cpf_1[5:8], cpf_1[8:])
celular_1 = input('celular:')
for celular in celular_1:
    if len(celular_1) >= 8:
        print("CELULAR INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        celular_1 = celular_1.zfill(8)
celular = '{}-{}'.format(celular_1[:4], celular_1[4:])
telefone_1 = input('telefone:')
for telefone in telefone_1:
    if len(telefone_1) >= 8:
        print("TELEFONE INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        telefone_1 = telefone_1.zfill(8)
telefone = '{}-{}'.format(telefone_1[:4], telefone_1[4:])
email = input("email: ")
obs = input("obs: ")
cep_1 = input('cep:')
for cep in cep_1:
    if len(cep_1) < 14:
        print("CEP INFORMADO ESTÁ NO FORMATO INCORRETO")
        os.system('python "fornecedorescad.py"')
    else:
        cep_1 = cep_1.zfill(8)
cep = '{}.{}-{}'.format(cep_1[:2], cep_1[2:5], cep_1[5:])
endereco = input("endereço: ")
numero = input("numero: ")
bairro = input("bairro: ")
cidade = input("cidade: ")
estado = input("estado: ")

for nome in 'nome':
    cursor.execute("SELECT count(*) FROM cliente WHERE nome = ?", (nome,))
    data = cursor.fetchone()[0]
if data == 0:
    cursor.execute('''
        INSERT INTO cliente ( nome, sobrenome, cpf, rg, celular, telefone, email, obs, cep, endereco, numero, bairro,
        cidade, estado)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (nome, sobrenome, cpf, rg, celular, telefone, email, obs,
                    cep, endereco, numero, bairro, cidade, estado))
    conn.commit()

    print('Dados inseridos com sucesso.')
    conn.close()
else:
    print("Error: Cliente ja Cadastrado.\n")
    sleep(5)
