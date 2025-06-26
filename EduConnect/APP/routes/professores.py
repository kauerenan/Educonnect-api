from flask import Blueprint, request, jsonify
from APP.models.professor_model import Professor
from APP.db.database import db

professores_routes = Blueprint("professores_routes", __name__)

@professores_routes.route("/professores", methods=["GET"])
def listar_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores cadastrados
    """
    professores = Professor.query.all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "especialidade": p.especialidade,
        "email": p.email
    } for p in professores])

@professores_routes.route("/professores", methods=["POST"])
def criar_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            especialidade:
              type: string
            email:
              type: string
    responses:
      201:
        description: Professor criado com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or not all(k in data for k in ("nome", "especialidade", "email")):
        return jsonify({"erro": "Dados incompletos"}), 400
    novo = Professor(**data)
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Professor criado com sucesso!"}), 201

@professores_routes.route("/professores/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    """
    Atualiza um professor existente
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            especialidade:
              type: string
            email:
              type: string
    responses:
      200:
        description: Professor atualizado com sucesso
      404:
        description: Professor não encontrado
    """
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "Professor não encontrado"}), 404
    data = request.get_json()
    for campo in ["nome", "especialidade", "email"]:
        if campo in data:
            setattr(prof, campo, data[campo])
    db.session.commit()
    return jsonify({"mensagem": "Professor atualizado com sucesso"})

@professores_routes.route("/professores/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    """
    Deleta um professor
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: Professor deletado com sucesso
      404:
        description: Professor não encontrado
    """
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "Professor não encontrado"}), 404
    db.session.delete(prof)
    db.session.commit()
    return jsonify({"mensagem": "Professor deletado com sucesso"})