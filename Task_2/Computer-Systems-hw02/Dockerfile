# Вказуємо базовий образ
FROM python:3.10

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл вимог у робочу директорію
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі файли з поточної директорії на робочу директорію в контейнері
COPY . .

# Відкриваємо порт 8000 для FastAPI
EXPOSE 8000

# Команда для запуску застосунку
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

