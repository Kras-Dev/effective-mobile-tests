# Dockerfile
# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR  /effective-mobile-tests

# Обновляем apt и устанавливаем системные зависимости для Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libasound2 \
    libatspi2.0-0 \
    libgtk-3-0 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libx11-xcb1 \
    libxcb1 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxi6 \
    libxtst6 \
    libgl1 \
    libegl1 \
    libopus0 \
    fonts-liberation \
    libappindicator3-1 \
    lsb-release \
    xdg-utils \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей и устанавливаем Python-зависимости проекта
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Устанавливаем браузеры Playwright вместе с зависимостями
RUN python -m playwright install --with-deps

# Команда для запуска тестов
CMD ["sh", "-c", "python -m pytest && allure generate -o ./allure-reports --clean && allure open ./allure-reports"]
