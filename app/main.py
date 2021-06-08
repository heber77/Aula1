from flask import request,Blueprint, render_template
from Classes_do_sistema.Suporte import Suporte

main  =  Blueprint ( 'main' , __name__ )


@main.route("/index")
def home():
    return render_template('index.html')

@main.route("/teste_gratis")
def testegratis():
    return render_template("teste_gratis.html")

@main.route("/cases")
def casesdesucesso():
    return render_template("cases.html")

@main.route("/duvidas")
def duvidasfrequentes():
    return render_template("duvidas.html")


@main.route("/lojadigital")
def lojadigital():
    return render_template("lojadigital.html")

@main.route("/lojafisica")
def lojafisica():
    return render_template("lojafisica.html")



@main.route("/suporte")
def suporte():
    return render_template("suporte.html")

@main.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@main.route("/cadastraCli", methods=["GET", "POST"])
def cadastrarCli():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email_c"]
        numero = request.form["numero"]
        data_de_nascimento = request.form["data_de_nascimento"]
        senha = request.form["senha"]
        return render_template("home.html")
    return "/cadastro"


@main.route("/envia", methods=["GET", "POST"])
def envia():
    if request.method == "POST":
        duvida = request.form["duvida"]
        suport = Suporte()
        print(suport.enviarDuvida(duvida))
        return render_template("index.html")
    return "/index"



