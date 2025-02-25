#importando uma parte do flask
from flask import Flask

#criando a variavel e instanciando
app = Flask(__name__)

#-------------------------------------------------------------------------------------------

@app.route("/")
def pagina_principal():
    return "ta"

#--------------------------------------------------------------------------------------------

app.run(debug = True)