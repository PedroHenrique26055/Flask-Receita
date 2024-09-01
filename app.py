from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

abs_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + abs_dir + "\\album-receitas.db"

db = SQLAlchemy(app)

from models import *
from views import *

# troquei o Migrate(app, db) por
with app.app_context(): 
    db.create_all()
    adiciona_usuario_adm() # Adicionando o usuário adm antes de iniciar a aplicação


if __name__ == '__main__':
    app.run(debug=True)