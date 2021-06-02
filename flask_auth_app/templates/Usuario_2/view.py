from os import name
from flask import Blueprint,render_template

#usuario de negocio digital
Usuario_2 = Blueprint('Usuario_2', __name__, template_folder='pages')

@Usuario_2.route("/templates/base")
def login():
    return render_template ('base_2.html', {{name}})

@Usuario_2.route("/templates/signup_2")
def signup():
    return render_template('signup_2.html', signup)

@Usuario_2.route("/templates/Usuario_2/pages/cases_sucesso")
def cases_sucesso():
    return render_template('cases_sucesso.html',cases_sucesso)

@Usuario_2.route("/templates/Usuario_2/pages/cases_sucesso_2")
def cases_sucesso_2():
    return render_template('cases_sucesso_2.html',cases_sucesso_2)

@Usuario_2.route("/templates/Usuario_2/pages/cases_sucesso_3")
def cases_sucesso_3():
    return render_template('cases_sucesso_3.html',cases_sucesso_3)

@Usuario_2.route("/templates/Usuario_2/pages/cases_sucesso_4")
def cases_sucesso_4():
    return render_template('cases_sucesso_4.html',cases_sucesso_4)

@Usuario_2.route("/templates/Usuario_2/pages/cases_sucesso_5")
def cases_sucesso_5():
    return render_template('cases_sucesso_5.html',cases_sucesso_5)

@Usuario_2.route("/templates/Usuario_2/pages/anexar_case")
def anexar_case():
    return render_template('anexar_case.html',anexar_case)

@Usuario_2.route("/templates/Usuario_2/pages/suporte")
def suporte():
    return render_template('suporte.html',suporte)

@Usuario_2.route("/templates/Usuario_2/pages/duvidas_txt")
def duvidas_txt():
    return render_template('duvidas_txt.html',duvidas_txt)

@Usuario_2.route("/templates/Usuario_2/pages/profile")
def profile():
    return render_template('profile.html',duvidas_txt)

@Usuario_2.route("/templates/Usuario_2/pages/cursos_adicionais")
def cursos_adicionais():
    return render_template('cursos_adicionais.html',cursos_adicionais)

@Usuario_2.route("/templates/Usuario_2/pages/curso")
def curso():
    return render_template('curso.html', curso)



from flask import Blueprint, render_template, redirect, url_for, request
#from werkzeug.security import generate_password_hash, check_password_hash
from  flask.ext.bcrypt  import  Bcrypt 
from .models import User
from . import db

...
@Usuario_2.route('/signup_2', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    data_nascimento = request.form.get('text')
    numero = request.form.get('numero')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('Usuario_2.index'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, data_nascimento=data_nascimento, numero = numero, password= Bcrypt.generate_password_hash(password, method='sha256'))
    auth_senha = Bcrypt
    new_user.check_password_hash ( new_user.select(password) , auth_senha )


    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.base_2'))

@Usuario_2.route("templates/signup_2", methods=['POST'])
def signup_post():
    ...
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))


from flask_login import login_user, logout_user, login_required,LoginManager,current_user
from __init__ import create_app
...

@Usuario_2.route("/templates/Usuario_2/pages/base_2")
@login_required
def sair():
    sair = request.form.get('next')
    logout_user(sair)
    return redirect(url_for('main.index'))

create_app
@Usuario_2.user_loader
def load_user(user_id):
    return User.get(user_id)

@Usuario_2.route("templates/base", methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)
        flask.flash('Logged in successfully.')
        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for("/templates/Usuario_2/pages/base_2"))
    return flask.render_template("base_2.html", form=form)


LoginManager.unauthorized_handler()
from flask import g
@Usuario_2.before_request
def load_users():
    if current_user.is_authenticated():
        g.user = current_user.get_id() # return username in get_id()
    else:
        g.user = None # or 'some fake value', whatever
    

current_user.is_authenticated


