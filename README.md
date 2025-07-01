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

2. Acesse a documentação Swagger:

   http://localhost:5000/apidocs

---

## 🛠️ Executar o Backend via PowerShell (opcional)

Se desejar rodar pelo script PowerShell:

- Edite o arquivo start_backend.ps1 e atualize o caminho do projeto:
  $projeto = "C:\Users\Kaue Renan\Desktop\EduConnect-api"
- Abra o PowerShell
- Navegue até a pasta backend:
  cd caminho\para\EduConnect-api\backend
- Execute:
  .\start_backend.ps1

---

## 🧪 Como testar a API no Postman

Você pode testar todos os endpoints diretamente no Postman:

### ✅ Opção 1: Importar arquivo `.json`

1. Abra o Postman Desktop ou Web
2. Clique em “Import” (canto superior esquerdo)
3. Selecione o arquivo Educonnect-api.postman_collection.json
4. Clique em “Import”
5. A collection “Educonnect-api” será carregada com todas as requisições prontas

⚠️ Certifique-se que a API esteja rodando em http://localhost:5000 antes de testar.

---

### ☁️ Opção 2: Importar via link (Postman Cloud)

Se preferir, use o link da collection salva na nuvem:

https://kauerenan.postman.co/workspace/Apresenta%C3%A7%C3%A3o-EduConnect~2e72d752-e900-47dc-8afe-3d3e848f7b18/collection/44028091-4a57a495-5dc8-4ec3-81da-420f502820d6

1. Acesse o link
2. Faça login no Postman
3. Clique em “Fork” ou “Import”
4. Acesse a collection no seu workspace

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

## 👁️ Visualizar o Banco de Dados (SQLite)

1. Abra o DBeaver
2. Crie uma nova conexão do tipo SQLite
3. Aponte para o arquivo:
   C:\Users\Administrador\Desktop\Educonnect-api-main\backend\instance\escola.db

---

## 📖 Documentação via Swagger

Após rodar o backend, acesse:

http://localhost:5000/apidocs

---

## 🚫 Arquivos ignorados (.gitignore)

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
