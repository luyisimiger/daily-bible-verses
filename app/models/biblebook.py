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
