from flask import render_template

from app import app
from app.models import BibleBook, BibleBookChapter

@app.route('/chapters/<int:id>')
def readchapter(id=1):

    chapter = BibleBookChapter.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/chapter.html', books = books, chapter = chapter)
