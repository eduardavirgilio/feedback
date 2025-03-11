import mysql.connector

#pastinha onde guarda metodos(funcoes) e atributos (caracteristicas)
class Conexao: 

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