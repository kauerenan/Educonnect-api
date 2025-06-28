from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///escolar.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # 👇 Importa as models ANTES de criar o banco
    from APP.models.aluno_model import Aluno
    from APP.models.turma_model import Turma

    with app.app_context():
        db.create_all()