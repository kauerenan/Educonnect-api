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

🛠️ Executar o Backend via PowerShell
Caso deseje utilizar o atalho via PowerShell, siga os passos abaixo:
- Ajuste o caminho do projeto no script
- No arquivo start_backend.ps1, edite o valor da variável:
$projeto = "C:\Users\Kaue Renan\Desktop\EduConnect-api"
- ⚠️ Este caminho deve refletir onde o projeto está localizado na sua máquina. Altere conforme necessário!
- Abra o terminal PowerShell e navegue até a pasta backend com:
cd caminho\para\EduConnect-api\backend
- Execute o script:
.\start_backend.ps1
- Esse comando irá:
- Derrubar containers antigos (se houver)
- Reconstruir as imagens Docker
- Iniciar o backend
- Abrir o navegador automaticamente com a interface Swagger


---

## 👁️ Visualizar os Dados do Banco

Para vizualizar  o banco, é só  acessar o DBEAVER
Adicionar o banco SQLITE em nova conexão e selecionar o escola.db
diretorio: C:\Users\Administrador\Desktop\Educonnect-api-main\backend\instance\escola.db


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
