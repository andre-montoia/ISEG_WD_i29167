#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"
#if __name__ == "__main__":
#    app.run()


import sqlite3
from sqlite3 import Error

##Criação de conexão
def caminho_bd ():
    """
        Criação de uma conexão para a base de dados. \n
        O Return é conexção à base de bados Lab_4.
    """
    caminho= "Lab_4.db" #C:\\Python\\ISEG_WD_i29243\\Lab_4\
    conexao = None
    try:
        conexao= sqlite3.connect(caminho)
    except Error as ex:
        print (ex)
    return conexao

vconexao= caminho_bd ()


##Criação de tabela

vsql = """CREATE TABLE IF NOT EXISTS tb_users (
    id_users INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT VARCHAR(30))"""
def tabela_db(conexao,vsql):
    """
    Criação da tabela "Users" na base de dados Lab_4. \n
    Necessário um cursor e um execute.
    """
    try:
        c=conexao.cursor()
        c.execute(vsql)
        print("tabela criada")
    except Error as ex:
        print (ex)  

tabela_db(vconexao,vsql)
vconexao.close()

##Inserção de novos dados na tabela tb_users
vconexao= caminho_bd ()

vsql= """INSERT INTO tb_users (name) 
        VALUES ( "Bernardo")""" #"Rafael",
        
def inserir(conexao,vsql):
    """Inserção de novos dados na tabela "Users" na base de dados Lab_4. \n
        Necessário um cursor, um execute e um commit."""

    try:
        c= conexao.cursor ()
        c.execute (vsql)
        conexao.commit ()
        print("dados adicionados com sucesso")
    except Error as ex:
        print (ex)
inserir(vconexao,vsql)

##Apagar dados na tabela (DELETE)

vsql="""DELETE FROM tb_users where id_users = 1"""

def apagar(conexao,vsql):
    """Remover dados na tabela "Users" na base de dados Lab_4. \n
       Necessário um cursor, um execute e um commit."""

    try:
        c= conexao.cursor ()
        c.execute (vsql)
        conexao.commit ()
    except Error as ex:
        print (ex)
    finally:
        print("dados removidos com sucesso")
apagar(vconexao,vsql)

##UpDate de dados na tabela

vsql= """UPDATE tb_users SET name = "Bernardo" WHERE id_users = 3"""

def update(conexao,vsql):
    """Atualização de dados na tabela "Users" na base de dados Lab_4. \n
        Necessário um cursor, um execute e um commit."""
    try:
        c= conexao.cursor ()
        c.execute (vsql)
        conexao.commit ()
    except Error as ex:
        print (ex)
    finally:
        print("dados atualizados com sucesso")
update(vconexao,vsql)

##Pesquisa de dados na tabela

def pesquisa(conexao,vsql):
    """Pesquisa de dados na tabela "Users" na base de dados Lab_4. \n
        Necessário um cursor, um execute. \n
        Vai ser criada uma nova tabela com os dados selecionados. \n
        Vamos receber um return: a pesquisa propriamente dita"""
    
    c= conexao.cursor ()
    c.execute (vsql)
    resultado= c.fetchall ()
    return resultado 

vsql= """SELECT * FROM tb_users"""  
#Para fazer a pesquisa em todas as linhas da tabela, temos de fazer um ciclo for. Para isso vamos transfomar a "pesquisa",
 #não a função mas a corrida numa variàvel. Assim...      
res = pesquisa(vconexao,vsql)  
for r in res:
    print (r) 
#Vai imprimir no terminal a informação de cada linha de toda a tabela
