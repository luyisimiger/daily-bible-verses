from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

URL = 'mysql://igle_bible:igle_bible@mysql-igle.alwaysdata.net/igle_bible'
#URL = 'sqlite:////media/sf_B_DRIVE/workspace/daily-bible-verses/bibleapp.db'

engine = create_engine(URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
