FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y sqlite3
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY eduapp ./eduapp
COPY app.py .
COPY ver_banco.py .
COPY instance ./instance
COPY wait-for-db.py .

EXPOSE 5000

CMD ["python", "app.py"]