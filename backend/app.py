from flask import Flask
from flasgger import Swagger
from APP.routes.alunos import alunos_routes
from APP.routes.professores import professores_routes
from APP.routes.turmas import turmas_routes
from APP.db.database import init_db

app = Flask(__name__)
init_db(app)

# Blueprint das rotas
app.register_blueprint(alunos_routes)
app.register_blueprint(professores_routes)
app.register_blueprint(turmas_routes)

# Configuração do Swagger (usando OpenAPI 3.0)
app.config["SWAGGER"] = {
    "title": "EduConnect API",
    "uiversion": 3,
    "openapi": "3.0.2",
    "specs_route": "/apidocs"
}

swagger = Swagger(app, parse=True)

# Cria tabelas no banco ao subir
with app.app_context():
    from APP.models import aluno_model, professor_model, turma_model
    aluno_model.db.create_all()
    professor_model.db.create_all()
    turma_model.db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)