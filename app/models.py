#import datetime
#import rtf

from app import db

class BibleBook(db.Model):
    __tablename__ = 'bible_books'

    id = db.Column('_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    testament = db.Column(db.String(1), nullable=False)
    chapters = db.Column(db.Integer, nullable=False)

    chapters_list = db.relationship("BibleBookChapter", back_populates="book", viewonly=True)

    def get_chapter(self, number):
        for chapter in self.chapters_list:
            if chapter.chapter == number:
                return chapter
        return None


class BibleBookChapter(db.Model):
    __tablename__ = 'bible_books_chapters'

    id = db.Column('_id', db.Integer, primary_key=True)
    idBook = db.Column(db.Integer, db.ForeignKey(BibleBook.id))
    chapter = db.Column(db.Integer, nullable=False)
    verses_count = db.Column('verses', db.Integer, nullable=False)
    
    book = db.relationship("BibleBook", back_populates="chapters_list")
    verses = db.relationship("BibleVerse", back_populates="chapter", viewonly=True)
    
    def __init__(self):
		self.verses = 0

class BibleVerse(db.Model):
    __tablename__ = 'bible_verses'

    id = db.Column('_id', db.Integer, primary_key=True)
    idBible = db.Column('idBible', db.Integer)
    idChapter = db.Column(db.Integer, db.ForeignKey(BibleBookChapter.id))
    verse = db.Column('verse', db.Integer)
    text = db.Column(db.String(1024), nullable=False)

    chapter = db.relationship("BibleBookChapter", back_populates="verses", uselist=False, viewonly=True)

    #def __str__(self):
    #    return rtf.to_plain_text(self.text)
