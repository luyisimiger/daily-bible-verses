from flask import render_template, request

from app import app
from app import babel
from config import LANGUAGES

from app.views.books import readbook
from app.views.chapters import readchapter
from app.views.verses import readverse

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/bible')
def bible_view():
    return readbook(1)

@app.route('/')
def index_view():
    return bible_view()

@app.route('/template/<path:file>')
def template_view(file):
    return render_template(file)
