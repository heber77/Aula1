from flask import Flask

app = Flask(__name__, template_folder='templates')  # por default use o nome da pasta templates

from app import cliente
from app import admin
from app import main