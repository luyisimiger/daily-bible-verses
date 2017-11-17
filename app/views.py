from flask import render_template

from app import app
from app.models import BibleBook, BibleBookChapter, BibleVerse

@app.route('/book/<int:id>')
def book_view(id):
    
    biblebook = BibleBook.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/book.html', books = books, book = biblebook)


@app.route('/chapters/<int:id>')
def chapter_view(id=1):
    
    chapter = BibleBookChapter.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/chapter.html', books = books, chapter = chapter)


@app.route('/verses/<int:id>')
def verse_view(id):
    
    verse = BibleVerse.query.get(id)
    books = BibleBook.query.all()
    return render_template('bibleapp/verse.html', books = books, verse = verse)


@app.route('/bible')
def bible_view():
    return book_view(1)

@app.route('/')
def index_view():
    return bible_view()