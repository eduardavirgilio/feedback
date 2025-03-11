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

#--------------------------------------------------------------------------------------------

app.run(debug = True)