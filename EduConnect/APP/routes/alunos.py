from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from APP.models.aluno_model import Aluno
from APP.db.database import db

alunos_routes = Blueprint("alunos_routes", __name__)

@alunos_routes.route("/alunos", methods=["GET"])
def listar_alunos():
    """
    Lista todos os alunos cadastrados
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  nome:
                    type: string
                    example: João da Silva
                  idade:
                    type: integer
                    example: 10
                  turma:
                    type: string
                    example: 5A
    """
    alunos = Aluno.query.all()
    return jsonify([
        {
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "turma": aluno.turma
        } for aluno in alunos
    ])

@alunos_routes.route("/alunos", methods=["POST"])
def criar_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - nome
              - idade
              - turma
            properties:
              nome:
                type: string
                example: Maria
              idade:
                type: integer
                example: 11
              turma:
                type: string
                example: 6B
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()

    if not data or not all(k in data for k in ("nome", "idade", "turma")):
        return jsonify({"erro": "Dados incompletos"}), 400

    novo_aluno = Aluno(
        nome=data["nome"],
        idade=data["idade"],
        turma=data["turma"]
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno criado com sucesso!"}), 201