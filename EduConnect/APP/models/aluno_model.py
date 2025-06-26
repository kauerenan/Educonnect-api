from APP.db.database import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma = db.Column(db.String(10), nullable=False)