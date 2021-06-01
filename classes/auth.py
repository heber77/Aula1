from flask import Blueprint
from app import db

# usuario test
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'

#usuario de negocio fisico
Usuario_1 = Blueprint('auth', __name__)

@Usuario_1.route('/login')
def login():
    return 'Login'

@Usuario_1.route('/signup')
def signup():
    return 'Signup'

@Usuario_1.route('/logout')
def logout():
    return 'Logout'

#usuario de negocio digital
Usuario_2 = Blueprint('auth', __name__)

@Usuario_2.route('/login')
def login():
    return 'Login'

@Usuario_2.route('/signup')
def signup():
    return 'Signup'

@Usuario_2.route('/logout')
def logout():
    return 'Logout'

from flask import Blueprint, render_template
...
# Admin
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

#Usuario de loja fisica
@Usuario_1.route('/login')
def login():
    return render_template('login.html')

@Usuario_1.route('/signup')
def signup():
    return render_template('signup.html')

#Usuario de loja virtual
@Usuario_2.route('/login')
def login():
    return render_template('login.html')

@Usuario_2.route('/signup')
def signup():
    return render_template('signup.html')

from flask import Blueprint, render_template, redirect, url_for
...
@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))

@Usuario_1.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('Usuario_1.login'))

from flask import Blueprint, render_template, redirect, url_for, request
#from werkzeug.security import generate_password_hash, check_password_hash
from  flask.ext.bcrypt  import  Bcrypt 
from .models import User
from app import db
...
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password= Bcrypt.generate_password_hash(password, method='sha256'))
    auth_senha = Bcrypt
    new_user.check_password_hash ( new_user.select(password) , auth_senha )


    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

from flask import Blueprint, render_template, redirect, url_for, request, flash
...
@auth.route('/signup', methods=['POST'])
def signup_post():
    ...
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

from flask_login import login_user, logout_user, login_required
...
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))