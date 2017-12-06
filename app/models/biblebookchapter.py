from app import db
from app.models.biblebook import BibleBook

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
