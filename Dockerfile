# Алхам 1: Python суулгасан суурь image ашиглана
FROM python:3.11-slim

# Алхам 2: Ажлын хавтас үүсгэж орно
WORKDIR /app

# Алхам 3: requirements.txt-ийг хуулж сангууд суулгана
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Алхам 4: бусад бүх файлуудыг хуулна
COPY . .

# Алхам 5: Порт нээх
EXPOSE 5020

# Алхам 6: App-ыг ажиллуулах
CMD ["python", "app.py"]
