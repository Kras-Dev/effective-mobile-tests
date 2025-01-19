#Dockerfile
# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR  /effective-mobile-tests

# Устанавливаем зависимости проекта
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Устанавливаем необходимые браузеры для Playwright:
RUN playwright install chromium

# Команда для запуска тестов
CMD ["sh", "-c", "python -m pytest && allure generate -o ./allure-reports --clean && allure open ./allure-reports"]
