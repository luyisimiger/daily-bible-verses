from flask import render_template

from app import app
from app.models import BibleBook

@app.route('/book/<int:id>')
def readbook(id):

    biblebook = BibleBook.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/book.html', books = books, book = biblebook)
