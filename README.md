# Sprint_6
Проект автотестов для тестирования приложения оформления заказа самокатов - https://qa-scooter.praktikum-services.ru/

- директория pages содержит описания локаторов элементов веб-страниц и методы для работы с ними
- директория tests содержит тесты

установка зависимостей:
pip install -r requirements.txt

запуск тестов:
pytest tests --alluredir=allure_result

открытие сформированного allure-отчета:
allure open allure_report