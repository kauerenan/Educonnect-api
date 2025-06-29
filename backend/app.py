from flask import Flask
from flasgger import Swagger

# Rotas da aplicação
from eduapp.routes.alunos import alunos_routes
from eduapp.routes.professores import professores_routes
from eduapp.routes.turmas import turmas_routes

# Inicialização do banco de dados
from eduapp.db.database import init_db

# Models importados para criação automática das tabelas
from eduapp.models import aluno_model, professor_model, turma_model

app = Flask(__name__)

# Inicializa o banco com a config (usando escolar.db como fallback se não houver DATABASE_URL)
init_db(app)

# Registro dos blueprints (rotas)
app.register_blueprint(alunos_routes)
app.register_blueprint(professores_routes)
app.register_blueprint(turmas_routes)

# Configuração da documentação Swagger
app.config["SWAGGER"] = {
    "title": "EduConnect API",
    "uiversion": 3,
    "openapi": "3.0.2",
    "specs_route": "/apidocs"
}

swagger = Swagger(app, parse=True)

# Cria todas as tabelas automaticamente ao subir
with app.app_context():
    aluno_model.db.create_all()
    professor_model.db.create_all()
    turma_model.db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)