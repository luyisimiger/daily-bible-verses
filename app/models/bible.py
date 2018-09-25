from app import db

class Bible(db.Model):
    __tablename__ = 'bible_bibles'

    id = db.Column('_id', db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    abreviation = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(255))
    fuente = db.Column(db.String(50))
    apocrifa = db.Column(db.Integer)
    fuertes = db.Column(db.Integer)
