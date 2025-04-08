import mysql.connector

#pastinha onde guarda metodos(funcoes) e atributos (caracteristicas)
class Conexao: 

    def criar_conexao():
        #criando a conexao
        
        conexao = mysql.connector.connect(
            host="bdgodofredo-alexstocco-93db.b.aivencloud.com",
            port= 27974,
            user="3ds",
            password="banana",
            database = "db_feedback"
            )
        
        return conexao