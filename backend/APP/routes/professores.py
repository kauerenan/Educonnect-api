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
                    example: Ana Paula
                  especialidade:
                    type: string
                    example: Matemática
                  email:
                    type: string
                    example: ana.paula@escola.com
    """
    professores = Professor.query.all()
    return jsonify([
        {
            "id": p.id,
            "nome": p.nome,
            "especialidade": p.especialidade,
            "email": p.email
        } for p in professores
    ])

@professores_routes.route("/professores", methods=["POST"])
def criar_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    parameters:
      - name: corpo
        in: body
        required: true
        schema:
          type: object
          required:
            - nome
            - especialidade
            - email
          properties:
            nome:
              type: string
              example: Juliana Alves
            especialidade:
              type: string
              example: Artes
            email:
              type: string
              example: juliana.alves@escola.com
    responses:
      201:
        description: Professor criado com sucesso
        content:
          application/json:
            example:
              mensagem: Professor criado com sucesso!
      400:
        description: Dados inválidos
        content:
          application/json:
            example:
              erro: Dados incompletos
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
      - name: id
        in: path
        required: true
        schema:
          type: integer
      - name: corpo
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: Maria Eduarda
            especialidade:
              type: string
              example: Física
            email:
              type: string
              example: maria.eduarda@escola.com
    responses:
      200:
        description: Professor atualizado com sucesso
        content:
          application/json:
            example:
              mensagem: Professor atualizado com sucesso
      404:
        description: Professor não encontrado
        content:
          application/json:
            example:
              erro: Professor não encontrado
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
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Professor deletado com sucesso
        content:
          application/json:
            example:
              mensagem: Professor deletado com sucesso
      404:
        description: Professor não encontrado
        content:
          application/json:
            example:
              erro: Professor não encontrado
    """
    prof = Professor.query.get(id)
    if not prof:
        return jsonify({"erro": "Professor não encontrado"}), 404
    db.session.delete(prof)
    db.session.commit()
    return jsonify({"mensagem": "Professor deletado com sucesso"})