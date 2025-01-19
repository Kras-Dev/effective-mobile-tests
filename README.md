# Автоматизация тестирования сайта effective-mobile.ru

## Установка

1. Клонируйте репозиторий:
   
bash
    ```git clone <URL>```
    ```cd effective-mobile-tests```

2. Установите зависимости:
   
bash
  ```pip install -r requirements.txt```
   

## Запуск тестов локально

Для запуска тестов выполните команду:
bash
    ```python -m pytest```

Для генерации и просмотра отчётов выполните команду:
bash
    ```allure generate -o ./allure-reports; allure open ./allure-reports```

## Запуск тестов в Docker

1. Соберите образ Docker:
bash
   ```docker build -t effective-mobile-tests .```

2. Запустите контейнер:
   
bash
   ```docker run --rm effective-mobile-tests```