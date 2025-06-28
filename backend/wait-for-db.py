import time
import psycopg2
import os

# Configurações vindas das variáveis de ambiente (docker-compose.yml)
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")
DB_NAME = os.getenv("DB_NAME", "escola")

# Loop de tentativa de conexão
while True:
    try:
        print(f"Tentando conectar a {DB_HOST}:{DB_PORT}...")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        conn.close()
        print("✅ Banco disponível! Iniciando aplicação...")
        break
    except Exception as e:
        print("⏳ Banco ainda não disponível. Aguardando...")
        time.sleep(2)

# Agora sim, inicia o app
import subprocess
subprocess.run(["python", "app.py"])