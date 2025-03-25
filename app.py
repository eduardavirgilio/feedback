#importando uma parte do flask
from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
#criando a variavel e instanciando
app = Flask(__name__)

#-------------------------------------------------------------------------------------------

@app.route("/")
def pagina_principal():

    #recuperar as mensagens
    mensagens = Mensagem.recuperar_mensagens()

    #enviar as mensagens pra o template
    
    return render_template("principal.html", mensagens = mensagens)


@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    usuario = request.form.get("nome-usuario")
    
    mensagem = request.form.get("comentario")

    # cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_meensagem(usuario, mensagem)
    
    return redirect("/")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):

    Mensagem.deletar_mensagem(codigo)

    return redirect("/")

@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect ("/")

@app.route("/put/mensagem/adicionar/deslike/<codigo>")
def tirar_curtida(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect ("/")

@app.route("/pagina-de-login")
def pagina_login():
    return render_template ("login.html")

@app.route("/pagina-de-cadastro")
def pagina_cadastro():
    return render_template ("cadastro.html")

@app.route("/post/cadastro", methods = ["POST"])
def post_cadastro():
    login = request.form.get("login-usuario")
    
    nome = request.form.get("cadastro-nome")

    senha = request.form.get("cadastro-senha")

    # cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_usuario(login, nome, senha)
    
    return redirect("/")


#--------------------------------------------------------------------------------------------

app.run(debug = True)