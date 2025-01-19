# Автоматизация тестирования сайта effective-mobile.ru

## Установка

1. Клонируйте репозиторий:
    ```git clone <URL>```
    ```cd effective-mobile-tests```

2. Установите зависимости:
  ```pip install -r requirements.txt```

3. Устанавливаем необходимые браузеры для Playwright:
   ```playwright install chromium```
   

## Запуск тестов локально

Для запуска тестов выполните команду:
    ```python -m pytest```

Для генерации и просмотра отчётов выполните команду:
    ```allure generate -o ./allure-reports; allure open ./allure-reports```

## Запуск тестов в Docker

1. Соберите образ Docker:
   ```docker build -t effective-mobile-tests .```

2. Запустите контейнер:   
   ```docker run --rm effective-mobile-tests```
