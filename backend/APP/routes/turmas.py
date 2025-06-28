from flask import Blueprint, request, jsonify
from APP.models.turma_model import Turma
from APP.db.database import db

turmas_routes = Blueprint("turmas_routes", __name__)

@turmas_routes.route("/turmas", methods=["GET"])
def listar_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas retornada com sucesso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              nome:
                type: string
              ano:
                type: string
    """
    turmas = Turma.query.all()
    return jsonify([{
        "id": t.id,
        "nome": t.nome,
        "ano": t.ano
    } for t in turmas])

@turmas_routes.route("/turmas", methods=["POST"])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            ano:
              type: string
    responses:
      201:
        description: Turma criada com sucesso
    """
    data = request.get_json()
    if not data or not all(k in data for k in ("nome", "ano")):
        return jsonify({"erro": "Dados incompletos"}), 400
    nova = Turma(**data)
    db.session.add(nova)
    db.session.commit()
    return jsonify({"mensagem": "Turma criada com sucesso!"}), 201

@turmas_routes.route("/turmas/<int:id>", methods=["PUT"])
def atualizar_turma(id):
    """
    Atualiza uma turma existente
    ---
    tags:
      - Turmas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            ano:
              type: string
    responses:
      200:
        description: Turma atualizada com sucesso
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404
    data = request.get_json()
    for campo in ["nome", "ano"]:
        if campo in data:
            setattr(turma, campo, data[campo])
    db.session.commit()
    return jsonify({"mensagem": "Turma atualizada com sucesso"})

@turmas_routes.route("/turmas/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    """
    Deleta uma turma
    ---
    tags:
      - Turmas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Turma deletada com sucesso
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404
    db.session.delete(turma)
    db.session.commit()
    return jsonify({"mensagem": "Turma deletada com sucesso"})