FROM python:3.11-slim

WORKDIR /app

# Garante que a pasta do banco exista e tenha permissões suficientes
RUN mkdir -p APP/db && chmod -R 777 APP/db

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY APP ./APP
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]