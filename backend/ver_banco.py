from app import app
from eduapp.models.aluno_model import Aluno
from eduapp.models.professor_model import Professor
from eduapp.models.turma_model import Turma

with app.app_context():
    print("=== Turmas ===")
    for t in Turma.query.all():
        print(f"{t.id}: {t.nome} — {t.ano} ({t.turno})")

    print("\n=== Alunos ===")
    for a in Aluno.query.all():
        turma = Turma.query.get(a.turma_id)
        print(f"{a.nome} ({a.idade} anos) — {turma.nome} {turma.ano} ({turma.turno})")

    print("\n=== Professores ===")
    for p in Professor.query.all():
        print(f"{p.nome} — {p.email}")