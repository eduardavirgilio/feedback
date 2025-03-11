from data.conexao import Conexao
import datetime

class Mensagem:
    def cadastrar_meensagem(usuario, mensagem):
        data_hora = datetime.datetime.today()
    
        #cadastrando as informações no banco de dados
        
        #criando a conexao
        
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o sql que sera executado
        
        sql = """INSERT INTO tbComentarios (
                    nome, 
                    comentarios,
                    data_hora)
                    
                VALUES (
                    %s, %s, %s)"""
                    
        valores = (usuario, mensagem, data_hora)
        
        #executando o comando sql
        cursor.execute(sql, valores)
        
        #confirmo a alteração
        conexao.commit()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def recuperar_mensagens():

        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True)
        
        sql = """select nome as usuario, 
                comentarios as mensagem, 
                data_hora from tbComentarios;"""

        
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado
    
