-- Tabela de Professores
CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100),
    email VARCHAR(100)
);

-- Tabela de Turmas (com turno)
CREATE TABLE turmas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano INT,
    turno VARCHAR(20),
    professor_id INT REFERENCES professores(id)
);

-- Tabela de Alunos (com FK para turma)
CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    turma_id INT REFERENCES turmas(id)
);

-- Tabela de Disciplinas (cada disciplina vinculada a uma turma)
CREATE TABLE disciplinas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT,
    turma_id INT REFERENCES turmas(id)
);