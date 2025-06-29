FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY eduapp ./eduapp
COPY app.py .
COPY instance ./instance
COPY wait-for-db.py .

EXPOSE 5000

CMD ["python", "wait-for-db.py"]