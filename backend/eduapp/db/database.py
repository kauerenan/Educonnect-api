from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    # Caminho absoluto para o banco escolar.db na pasta instance
    caminho_absoluto = os.path.join(os.path.dirname(__file__), '../../instance/escolar.db')
    uri = f"sqlite:///{os.path.abspath(caminho_absoluto)}"

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print("[DEBUG] URI do banco:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    # 👇 Importa os models ANTES de criar o banco
    from eduapp.models.aluno_model import Aluno
    from eduapp.models.turma_model import Turma

    with app.app_context():
        db.create_all()