ℹ️ Acesse a documentação interativa da API em: http://localhost:5000/apidocs

# 🎓 EduConnect API

Este é o backend do **sistema de gestão escolar EduConnect**, desenvolvido para uma escola infantil. A API RESTful foi construída com **Python e Flask**, fornecendo operações CRUD completas para as entidades **Alunos**, **Professores** e **Turmas**, com integração a um banco de dados relacional e documentação automática via Swagger.

---

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- Flasgger (Swagger/OpenAPI)
- Docker

---

## 📁 Estrutura do Projeto

educonnect/ ├── APP/ │   ├── db/ │   ├── models/ │   ├── routes/ │   └── init.py ├── app.py ├── Dockerfile ├── requirements.txt └── README.md

---

## 🧠 Arquitetura do Backend

- **Modularização com Blueprints**: cada entidade possui suas rotas em arquivos separados.
- **ORM com SQLAlchemy**: mapeamento das tabelas do banco de dados.
- **Inicialização Centralizada**: tudo começa por `app.py`.
- **Swagger UI**: acessível para visualização e testes da API RESTful.

---

## 🐳 Executando com Docker

### 1. Build da Imagem

```bash
docker build -t educonnect-api .


2. Executar o Container
docker run -d -p 5000:5000 educonnect-api


Documentação Swagger: http://localhost:5000/apidocs

📬 Exemplos de Requisições
➕ Criar Aluno
POST /alunos
Content-Type: application/json

{
  "nome": "Maria Clara",
  "idade": 5,
  "id_turma": 1
}


📚 Obter Todos os Professores
GET /professores


✏️ Atualizar Turma
PUT /turmas/2
Content-Type: application/json

{
  "nome": "Turma Girassol"
}


❌ Remover Aluno
DELETE /alunos/4



📖 Acesso à Documentação
Após rodar a aplicação, acesse:
👉 http://localhost:5000/apidocs para a interface interativa do Swagger (OpenAPI 3.0)

👨‍💻 Autor
Desenvolvido por Kauê Renan Ferreora Barros
RA 6323069
Disciplina: Integração de Software



