from hashlib import sha256
from data.conexao import Conexao
from flask import session

class Usuario:
    def cadastrar(usuario, senha, nome):
        #criptografando a senha

        senha = sha256(senha.encode()).hexdigest()
        #cadastrando as informações no banco de dados
            
        #criando a conexao
            
        conexao = Conexao.criar_conexao()
            
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o sql que sera executado
            
        sql = """INSERT INTO tb_usuarios (
                        login, 
                        senha,
                        nome)
                        
                    VALUES (
                        %s, %s, %s)"""
                        
        valores = (usuario, senha, nome)
            
        #executando o comando sql
        cursor.execute(sql, valores)
            
        #confirmo a alteração
        conexao.commit()
            
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def logar(usuario, senha):
        #criptografando a senha

        senha = sha256(senha.encode()).hexdigest()
        #cadastrando as informações no banco de dados
            
        #criando a conexao
            
        conexao = Conexao.criar_conexao()
            
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor(dictionary=True)

        #criando o sql que sera executado
            
        sql = """SELECT login, nome from tb_usuarios
                WHERE login = %s and binary senha = %s; """
                        
        valores = (usuario, senha)
            
        #executando o comando sql
        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        conexao.close()
        cursor.close()

        if resultado:
            session["usuario"] = resultado['login']
            session["nome-usuario"] = resultado['nome']
            return True
        
        else:
            return False
        
    def logoff():
        session.clear()
            
        