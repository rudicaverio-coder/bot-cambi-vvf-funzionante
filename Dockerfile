FROM python:3.9-slim

WORKDIR /app

# Installa dipendenze di sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Installa dipendenze Python
RUN pip install --no-cache-dir \
    python-telegram-bot==20.7 \
    requests==2.31.0 \
    psutil==5.9.5

CMD ["python", "bot.py"]
