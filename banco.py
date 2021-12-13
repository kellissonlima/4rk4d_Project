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
def tabela():
    conn = sqlite3.connect('dbservos.db')
    print("Opened database successfully")
    conn.execute("""
    CREATE TABLE servos_info (
        id INT PRIMARY KEY NOT NULL,
        titulo TEXT NOT NULL, 
        valor REAL NOT NULL, 
        data DATA  NOT NULL
        );
    """)
    print("Table created successfully")
    conn.close()