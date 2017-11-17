import os

if __name__ == "__main__":
    os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, UniqueConstraint
from db import db_session
from models import BibleBook, BibleBookChapter, BibleVerse


q = db_session.query(BibleBook).filter(BibleBook.id==1)
b = q.first()

print str(q)

for r in range(1,b.chapters):
    chapter = b.get_chapter(r)
    print "chapter %d, verses %d, %s" % (chapter.chapter, chapter.verses_count, chapter.verses)
