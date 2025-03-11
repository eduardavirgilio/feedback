import mysql.connector

def criar_conexao():
     #criando a conexao
    
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port= 3306,
        user="root",
        password="root",
        database = "dbComentarios"
        )
    
    return conexao