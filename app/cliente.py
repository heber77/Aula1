from app import app
from flask import request, Blueprint,render_template
from Classes_do_sistema.Suporte import Suporte

cliente  =  Blueprint ( 'main' , __name__ )


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/testegratis")
def testegratis():
    return render_template("testegratis.html")

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

@app.route("/pagamentos")
def pagamentos():
    return render_template("pagamentos.html")

@app.route("/pagamentos/pix")
def pix():
    return render_template("pix.html")

@app.route("/pagamentos/boleto")
def boleto():
    return render_template("boleto.html")

@app.route("/pagamentos/cartao")
def cartao():
    return render_template("cartao.html")

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

@app.route("/aulas")
def aulas():
    return render_template("aulas.html")

@app.route("/suporte")
def suporte():
    return render_template("suporte.html")


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


@app.route("/envia", methods=["GET", "POST"])
def envia():
    if request.method == "POST":
        duvida = request.form["duvida"]
        suport = Suporte()
        print(suport.enviarDuvida(duvida))
        return render_template("index.html")
    return "/index"


