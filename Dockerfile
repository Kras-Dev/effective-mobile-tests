# Используем официальный образ Playwright с Python и предустановленными браузерами (Chromium, Firefox, WebKit)
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /effective-mobile-tests

# Устанавливаем системные зависимости:
# - openjdk-17-jdk — для запуска Allure (Java-приложение)
# - unzip, wget — для скачивания и распаковки Allure CLI
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/* \  # очищаем кеш apt для уменьшения размера образа
    # Скачиваем Allure CLI нужной версии
    && wget -qO allure.zip https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.zip \
    # Распаковываем Allure в /opt/
    && unzip allure.zip -d /opt/ \
    # Создаём символическую ссылку для удобного вызова allure из любого места
    && ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure \
    # Удаляем архив, чтобы не занимал место
    && rm allure.zip

# Копируем файл зависимостей Python в контейнер
COPY requirements.txt .

# Устанавливаем Python-зависимости без кеша pip (уменьшает размер образа)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код проекта в контейнер
COPY . .

# Chromium уже установлен в базовом образе, но если нужно — обновляем браузер
RUN python -m playwright install chromium

# Команда по умолчанию при запуске контейнера:
# 1. Запускаем pytest с генерацией результатов для Allure в ./allure-results
# 2. Генерируем HTML-отчёт Allure в ./allure-reports, предварительно очищая старый отчёт
# 3. Запускаем Allure сервер для просмотра отчёта, слушая на 0.0.0.0:5050 (чтобы порт был доступен снаружи)

CMD ["sh", "-c", "python -m pytest --alluredir=./allure-results && allure generate -o ./allure-reports --clean ./allure-results && allure open -h 0.0.0.0 -p 5050 ./allure-reports"]
