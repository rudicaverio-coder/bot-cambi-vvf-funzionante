FROM python:3.9-slim 
 
WORKDIR /app 
 
COPY . . 
 
RUN pip install --no-cache-dir \ 
    python-telegram-bot==20.7 \ 
    requests==2.31.0 
 
CMD ["python", "bot.py"] 
