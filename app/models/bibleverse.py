from app import db
from app.models.biblebookchapter import BibleBookChapter

class BibleVerse(db.Model):
    __tablename__ = 'bible_verses'

    id = db.Column('_id', db.Integer, primary_key=True)
    idBible = db.Column('idBible', db.Integer)
    idChapter = db.Column(db.Integer, db.ForeignKey(BibleBookChapter.id))
    verse = db.Column('verse', db.Integer)
    text = db.Column(db.String(1024), nullable=False)

    chapter = db.relationship("BibleBookChapter", back_populates="verses", uselist=False, viewonly=True)
