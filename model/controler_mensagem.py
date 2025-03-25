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
        
        sql = """INSERT INTO tb_comentarios (
                    nome, 
                    comentario,
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

        cursor = conexao.cursor(dictionary = True) #o dictionary é pra recuperar dados
        
        sql = """select nome as usuario, 
                comentario as mensagem,
                cod_comentario,
                data_hora,
                curtidas from tb_comentarios;"""

        
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado
    
    def deletar_mensagem(codigo):
        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()
        
        sql = """delete from tb_comentarios where cod_comentario = %s;
        """

        valor = (codigo,) #coloca a , pra saber que é uma tupla
        #executando o comando sql
        cursor.execute(sql, valor)

        #comitando
        conexao.commit()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()
    
    def curtir_mensagem(codigo):
        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()
        
        sql = """UPDATE tb_comentarios 
        SET curtidas = curtidas + 1
        WHERE cod_comentario = %s;
        """

        valor = (codigo,) #coloca a , pra saber que é uma tupla
        #executando o comando sql
        cursor.execute(sql, valor)

        #comitando
        conexao.commit()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def descurtir_mensagem(codigo):
        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()
        
        sql = """UPDATE tb_comentarios 
        SET curtidas = curtidas - 1
        WHERE cod_comentario = %s;
        """

        valor = (codigo,) #coloca a , pra saber que é uma tupla
        #executando o comando sql
        cursor.execute(sql, valor)

        #comitando
        conexao.commit()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def cadastrar_usuario(usuario, nome, senha):
        data_hora = datetime.datetime.today()
    
        #cadastrando as informações no banco de dados
        
        #criando a conexao
        
        conexao = Conexao.criar_conexao()
        
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o sql que sera executado
        
        sql = """INSERT INTO tb_usuarios (
                    login, 
                    nome,
                    senha)
                    
                VALUES (
                    %s, %s, %s)"""
                    
        valores = (usuario, nome, senha)
        
        #executando o comando sql
        cursor.execute(sql, valores)
        
        #confirmo a alteração
        conexao.commit()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()