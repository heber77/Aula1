from flask import request, Blueprint, render_template, url_for, redirect, flash
from .models import User
from flask_bcrypt import Bcrypt
#Banco de dados
from . import db

main = Blueprint('main', __name__)


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


# @app.route("/envia", methods=["GET", "POST"])
# def envia():
# if request.method == "POST":
# duvida = request.form["duvida"]
# suport = Suporte()
# print(suport.enviarDuvida(duvida))
# return render_template("home.html")
# return "/home"


@main.route("/lojadigital", methods=['POST'])
def lojadigital_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    data_nascimento = request.form.get('text')
    numero = request.form.get('numero')

    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('main.'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, data_nascimento=data_nascimento, numero=numero,
                    password=Bcrypt.generate_password_hash(password, method='sha256'))
    auth_senha = Bcrypt
    new_user.check_password_hash(new_user.select(password), auth_senha)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('cliente.index_cliente'))


@main.route("/lojadigital", methods=['POST'])
def lojadigital():
    if User:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email adicionado já existente')
        return redirect(url_for('main.lojadigital'))
