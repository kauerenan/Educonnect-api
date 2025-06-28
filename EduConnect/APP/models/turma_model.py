from APP.db.database import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.String(10))
    turno = db.Column(db.String(20), nullable=True)  # 👈 Novo campo adicionado