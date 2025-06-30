# 🎓 EduConnect API

EduConnect é uma API RESTful para gestão escolar, desenvolvida para uma escola infantil, permitindo o controle de alunos, turmas e professores. O projeto é modularizado com Flask e SQLAlchemy, containerizado com Docker e documentado via Swagger (Flasgger).

ℹ️ Documentação interativa disponível em: http://localhost:5000/apidocs

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Flask + Blueprints
- SQLAlchemy (ORM)
- Flasgger (Swagger UI)
- SQLite (armazenado em backend/instance/escolar.db)
- Docker + Docker Compose

---

## 🧱 Estrutura de Pastas

EduConnect-api/
├── backend/
│   ├── app/                  # Módulo principal do app Flask
│   │   ├── db/               # Conexão com o banco
│   │   ├── models/           # Modelos ORM
│   │   ├── routes/           # Rotas por entidade
│   │   └── __init__.py
│   ├── app.py                # Ponto de entrada Flask
│   ├── ver_banco.py          # Script para consultar o banco
│   ├── requirements.txt
│   └── instance/             # Arquivos locais (como escolar.db)
├── docker-compose.yml
└── start_backend.ps1

---

## 🐳 Como Rodar com Docker

1. Subir a aplicação:

docker compose up --build

Ou, para rodar em segundo plano:

docker compose up -d

Swagger: http://localhost:5000/apidocs

---

## ✅ Atalho via PowerShell

Se preferir, execute:

& "backend/start_backend.ps1"

Este script:
- Derruba containers antigos
- Reconstrói imagens
- Aguarda backend subir
- Abre o navegador com o Swagger

---

## 👁️ Visualizar os Dados do Banco

Você pode rodar o script abaixo para exibir turmas, alunos e professores cadastrados:

docker exec -it educonnect-backend python ver_banco.py

O script está localizado em: backend/ver_banco.py

---

## 🔄 Exemplos de Requisições (JSON)

➕ Criar Aluno

POST /alunos
{
  "nome": "Maria Clara",
  "data_nascimento": "2017-10-05",
  "turma_id": 1
}

📚 Listar Professores

GET /professores

✏️ Atualizar Turma

PUT /turmas/2
{
  "nome": "Turma Girassol",
  "ano": "2025",
  "turno": "Tarde"
}

❌ Deletar Aluno

DELETE /alunos/4

---

## 📖 Documentação Swagger

Após rodar a aplicação, acesse:
http://localhost:5000/apidocs

---

## 🚫 Arquivos ignorados (via .gitignore)

Certifique-se de incluir um .gitignore contendo:

__pycache__/
*.pyc
*.db
instance/
.env

---

## 👨‍💻 Autor

Desenvolvido por Kauê Renan Ferreira Barros  
RA: 6323069  
Disciplina: Integração de Software e Implementação de Software