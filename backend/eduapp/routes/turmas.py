from flask import Blueprint, request, jsonify
from eduapp.models.turma_model import Turma
from eduapp.db.database import db

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
        content:
          application/json:
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
                  turno:
                    type: string
    """
    turmas = Turma.query.all()
    return jsonify([
        {
            "id": t.id,
            "nome": t.nome,
            "ano": t.ano,
            "turno": t.turno
        } for t in turmas
    ])


@turmas_routes.route("/turmas", methods=["POST"])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - nome
              - ano
            properties:
              nome:
                type: string
                example: 5º A
              ano:
                type: string
                example: 2025
              turno:
                type: string
                example: Manhã
    responses:
      201:
        description: Turma criada com sucesso
        content:
          application/json:
            example:
              mensagem: Turma criada com sucesso!
      400:
        description: Dados inválidos
        content:
          application/json:
            example:
              erro: Dados incompletos
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
              ano:
                type: string
              turno:
                type: string
    responses:
      200:
        description: Turma atualizada com sucesso
        content:
          application/json:
            example:
              mensagem: Turma atualizada com sucesso
      404:
        description: Turma não encontrada
        content:
          application/json:
            example:
              erro: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    data = request.get_json()
    for campo in ["nome", "ano", "turno"]:
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
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Turma deletada com sucesso
        content:
          application/json:
            example:
              mensagem: Turma deletada com sucesso
      404:
        description: Turma não encontrada
        content:
          application/json:
            example:
              erro: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    db.session.delete(turma)
    db.session.commit()
    return jsonify({"mensagem": "Turma deletada com sucesso"})