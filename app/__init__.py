from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder='templates')  # por default use o nome da pasta templates
bcrypt = Bcrypt(app)

from app import cliente
from app import admin
from app import main