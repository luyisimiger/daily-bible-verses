from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
android_metadata = Table('android_metadata', pre_meta,
    Column('locale', TEXT),
)

bible_bibles = Table('bible_bibles', pre_meta,
    Column('_id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=255), nullable=False),
    Column('abreviation', VARCHAR(length=50), nullable=False),
    Column('comment', VARCHAR(length=255)),
    Column('fuente', VARCHAR(length=50)),
    Column('apocrifa', INTEGER),
    Column('fuertes', INTEGER),
)

bible_books_references = Table('bible_books_references', pre_meta,
    Column('_id', INTEGER, primary_key=True, nullable=False),
    Column('idBook', INTEGER, nullable=False),
    Column('text', VARCHAR(length=20), nullable=False),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['android_metadata'].drop()
    pre_meta.tables['bible_bibles'].drop()
    pre_meta.tables['bible_books_references'].drop()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['android_metadata'].create()
    pre_meta.tables['bible_bibles'].create()
    pre_meta.tables['bible_books_references'].create()
    post_meta.tables['user'].drop()
