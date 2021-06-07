from app import app
from flask import request, render_template
from Classes_do_sistema.Suporte import Suporte

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

#@app.route("/teste_gratis")
#def testegratis():
    #return render_template("teste_gratis.html")

@app.route("/cases")
def casesdesucesso():
    return render_template("cases.html")

@app.route("/duvidas")
def duvidasfrequentes():
    return render_template("duvidas.html")


@app.route("/lojadigital")
def lojadigital():
    return render_template("lojadigital.html")

@app.route("/lojafisica")
def lojafisica():
    return render_template("lojafisica.html")



#@app.route("/suporte")
#def suporte():
    #return render_template("suporte.html")

#@app.route("/cadastro")
#def cadastro():
    #return render_template("cadastro.html")

#@app.route("/cadastraCli", methods=["GET", "POST"])
#def cadastrarCli():
    #if request.method == "POST":
        #nome = request.form["nome"]
        #email = request.form["email_c"]
        #numero = request.form["numero"]
        #data_de_nascimento = request.form["data_de_nascimento"]
        #senha = request.form["senha"]
        #return render_template("home.html")
    #return "/cadastro"


#@app.route("/envia", methods=["GET", "POST"])
#def envia():
    #if request.method == "POST":
        #duvida = request.form["duvida"]
        #suport = Suporte()
        #print(suport.enviarDuvida(duvida))
        #return render_template("home.html")
    #return "/home"

