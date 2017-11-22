from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
babel = Babel(app)

from app import views
