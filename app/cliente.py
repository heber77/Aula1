from app import app
from flask import request, render_template
from classes.Suporte import Suporte

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/suporte")
def suporte():
    return render_template("suporte.html")

@app.route("/envia", methods=["GET", "POST"])
def envia():
    if request.method == "POST":
        duvida = request.form["duvida"]
        suport = Suporte()
        print(suport.enviarDuvida(duvida))
        return render_template("home.html")
    return "/home"

