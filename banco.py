import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)
print('End banco: ',pastaApp)
nomeBanco=pastaApp+'\\dbservos.db'

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con
def dql(query): #Função de Select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res
def dml(query): #Insert,update, delete
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        print('Fez a Função DML Requerida!\n')
    except Error as ex:
        print(ex)
#Criar a tabela
def tabela():
    conn = sqlite3.connect('dbservos.db')
    print("Opened database successfully")
    conn.execute("""
    CREATE TABLE servos_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        titulo TEXT NOT NULL, 
        valor REAL NOT NULL, 
        data DATA  NOT NULL,
        esq INT NOT NULL,
        dir INT NOT NULL
        );
    """)
    print("Table created successfully")
    conn.close()
#Situação da Tabela se ela se encontra populada
def situacaoTabela():
    query = "SELECT COUNT(*) FROM servos_info"
    curl = dql(query)
    print("O que tem no Banco de Dados: ",curl[0][0])
    if (curl[0][0] != 0):
        print(curl[0][0])
        print("Tem Registros na Tabela")
        return 1
    else:
        print("Não Tem Registros na Tabela")
        return 0
#Pegar os dados pelo ID
def consultaID(id):
    query = "SELECT * FROM servos_info WHERE ID = " + str(id)
    curl = dql(query)
    print("O que tem no Banco de Dados: ",curl)
    return curl[0][0]

def noReferencia():
    query = "SELECT COUNT(*) FROM servos_info"
    curl = dql(query)
    print("O que tem no Banco de Dados: ",curl[0][0])
    return curl[0][0]