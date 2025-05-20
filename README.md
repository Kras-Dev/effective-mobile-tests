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

Для генерации и просмотра отчётов выполните команды:
    ```allure generate -o ./allure-reports; allure open ./allure-reports```

## Запуск тестов в Docker

1. Соберите образ Docker:
   ```docker build -t effective-mobile-tests .```

2. Запустите контейнер и выполните тесты с генерацией отчёта (без открытия отчёта в браузере):  
   ```docker run --rm effective-mobile-tests```

3. Запустите контейнер с пробросом порта 5050 для просмотра отчёта Allure в браузере
    ```docker run -p 5050:5050 effective-mobile-tests```
4. После запуска откройте в браузере:
    ```http://localhost:5050```

5. (Опционально) Для сохранения результатов и отчётов на хост-машине используйте монтирование директорий:
    ```
   docker run --rm -p 5050:5050
    -v $(pwd)/allure-results:/effective-mobile-tests/allure-results
    -v $(pwd)/allure-reports:/effective-mobile-tests/allure-reports
    effective-mobile-tests
   ```