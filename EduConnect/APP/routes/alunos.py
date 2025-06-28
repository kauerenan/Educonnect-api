from flask import Blueprint, jsonify, request
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
        content:
          application/json:
            example:
              mensagem: Aluno criado com sucesso!
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

@alunos_routes.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    """
    Atualiza os dados de um aluno existente
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              idade:
                type: integer
              turma:
                type: string
    responses:
      200:
        description: Aluno atualizado com sucesso
        content:
          application/json:
            example:
              mensagem: Aluno atualizado com sucesso!
      404:
        description: Aluno não encontrado
    """
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    data = request.get_json()
    aluno.nome = data.get("nome", aluno.nome)
    aluno.idade = data.get("idade", aluno.idade)
    aluno.turma = data.get("turma", aluno.turma)

    db.session.commit()
    return jsonify({"mensagem": "Aluno atualizado com sucesso!"})

@alunos_routes.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    """
    Deleta um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Aluno deletado com sucesso
        content:
          application/json:
            example:
              mensagem: Aluno deletado com sucesso!
      404:
        description: Aluno não encontrado
    """
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno deletado com sucesso!"})