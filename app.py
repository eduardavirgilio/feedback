#importando uma parte do flask
from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data import conexao
#criando a variavel e instanciando
app = Flask(__name__)

#-------------------------------------------------------------------------------------------

@app.route("/")
def pagina_principal():
    return render_template("principal.html")


@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    usuario = request.form.get("nome-usuario")
    
    mensagem = request.form.get("comentario")
    
    data_hora = datetime.datetime.today()
    
    #cadastrando as informações no banco de dados
    
    #criando a conexao
    
    conexao = conexao.criar_conexao()
    
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

    return redirect("/")

#--------------------------------------------------------------------------------------------

app.run(debug = True)