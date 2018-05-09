from flask import render_template

from app import app
from app.models import BibleBook, BibleVerse

@app.route('/verses/<int:id>')
def readverse(id):

    verse = BibleVerse.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/verse.html', books = books, verse = verse)
