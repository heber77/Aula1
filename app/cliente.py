from flask import request, Blueprint,render_template,url_for, redirect, flash
from Classes_do_sistema.Suporte import Suporte
from flask_login import login_user, logout_user, login_required,LoginManager,current_user
from .models import User
from app import app
import flask
from flask_session import sessions

cliente  =  Blueprint ( 'main' , __name__ )
@cliente.route("/")
@cliente.route("/index_cliente")
def home():
    return render_template('index.html')



@cliente.route("/cases")
def casesdesucesso():
    return render_template("cases.html")

@cliente.route("/duvidas")
def duvidasfrequentes():
    return render_template("duvidas.html")


#@cliente.route("/lojadigital")
#def lojadigital():
    #return render_template("lojadigital.html")

#@cliente.route("/lojafisica")
#def lojafisica():
    #return render_template("lojafisica.html")



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


@cliente.route("/envia", methods=["GET", "POST"])
def envia():
    if request.method == "POST":
        duvida = request.form["duvida"]
        suport = Suporte()
        print(suport.enviarDuvida(duvida))
        return render_template("home.html")
    return "/home"

@cliente.route("/pagamentos")
def pagamentos():
    return render_template("pagamentos.html")

@cliente.route("/aulas")
def aulas():
    return render_template("aulas.html")

@cliente.route("/templates/index_cliente")
@login_required
def sair():
    sair = request.form.get('next')
    logout_user(sair)
    return redirect(url_for('main.index'))

app
@cliente.user_loader
def load_user(user_id):
    return User.get(user_id)


class LoginForm(User):

    pass


@cliente.route("index", methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=True)
            sessions.permanent = True
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid username or password.')
        return flask.redirect(next or flask.url_for("/templates/Usuario_2/pages/base_2"))
    return flask.render_template("base_2.html", form=form)