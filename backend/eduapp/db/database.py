import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Caminho absoluto até o banco escolar.db na pasta instance
    caminho_banco = os.path.join(app.root_path, 'instance', 'escolar.db')
    uri = f"sqlite:///{caminho_banco}"

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("[DEBUG] URI do banco:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    # Importa os models ANTES do create_all
    from eduapp.models.aluno_model import Aluno
    from eduapp.models.turma_model import Turma
    from eduapp.models.professor_model import Professor

    with app.app_context():
        db.create_all()