import mysql.connector

#pastinha onde guarda metodos(funcoes) e atributos (caracteristicas)
class Conexao: 

    def criar_conexao():
        #criando a conexao
        
        conexao = mysql.connector.connect(
            host="10.110.131.22",
            port= 3306,
            user="3ds",
            password="banana",
            database = "db_feedback"
            )
        
        return conexao