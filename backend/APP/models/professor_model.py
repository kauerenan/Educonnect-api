from APP.db.database import db

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    especialidade = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)