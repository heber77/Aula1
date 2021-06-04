from flask import Blueprint,render_template
from flask_auth_app import db

main = Blueprint('main', __name__)

@main.route("/templates/")
def index():
    return render_template('index.html')



@main.route("/templates/teste_gratis")
def teste_gratis():
    return render_template('teste_gratis.html')

@main.route("/templates/signup")
def signup():
    return render_template('signup.html', signup)

@main.route("/templates/cases_sucesso")
def cases_sucesso():
    return render_template('cases_sucesso.html', cases_sucesso)

@main.route("/templates/cases_sucesso_2")
def cases_sucesso_2():
    return render_template('cases_sucesso_2.hmtl', cases_sucesso_2)

@main.route("/templates/cases_sucesso_3")
def cases_sucesso_3():
    return render_template('cases_sucesso_3.html', cases_sucesso_3)

@main.route("/templates/cases_sucesso_4")
def cases_sucesso_4():
    return render_template('cases_sucesso_4.html', cases_sucesso_4)

@main.route("/templates/cases_sucesso_5")
def cases_sucesso_5():
    return render_template('cases_sucesso_5.html', cases_sucesso_5)

@main.route("/templates/duvidas_frequentes")
def duvidas_frequentes():
    return render_template('duvidas_frequentes.html', duvidas_frequentes)

@main.route("/templates/Suporte")
def suporte():
    return render_template('Suporte.html', suporte)

@main.route("/templates/cursos")
def cursos():
    return render_template('cursos.html', cursos)
