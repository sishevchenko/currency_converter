***
Author: sishevchenko  
GitHub: https://github.com/sishevchenko  
Telegram: @s_i_shevchenko  
***

# Currency Converter
> [!NOTE]
> The goal of the project is to develop an API for currency conversion using FastAPI and SQLAlchemy.  
> The API should provide the ability to get up-to-date exchange rates and convert between them.  

## Stages
### 1. Getting current exchange rates
- Create a model for storing information about the currency (name, code, rate).  
- Implement a function that will request current exchange rates from an external API and store them in the database.  

### 2. Conversion between currencies
- Implement a function that will accept two currencies as input (source and target) and the amount to be converted.  
- The function should return the conversion result based on the current exchange rates from the database.  

### 3. Creating and configuring API
- Using FastAPI, create an API with two endpoints: one for getting current exchange rates, the other for converting between currencies.  
- Set up interaction with the database using SQLAlchemy.  

> [!TIP]
> To fill and update the database, I used the API https://www.exchangerate-api.com/  


## STARTING AND OPERATION
### Preparatory stage
- To run the project, you need to install Python (3.11 is desirable)
- Through the terminal in the project folder, configure the virtual environment with the command python -m venv venv
- Enter the command pip install -r src/requirements/prod.txt to download the required libraries
- In the .env file, specify the parameters of the database and connection to the API https://www.exchangerate-api.com/
- Next, to configure the necessary tables in the database, enter the command alembic revision --autogenerate -m "YOUR-DB-NAME"
- Apply alembic migrations with alembic upgrade head command
- Check the correct operation by entering the command from the main directory of the uvicorn project src.main:app
- After a successful run in test mode, go to src/config.py and change the changed DEBUG = False
- Run the project with the uvicorn src.main:app command
- Wait some time for database update

### Working with API
- To get all currencies available for conversion: BASE-URL/currency/supported  
- To get all currency codes with conversion rate: BASE-URL/currency/all  
- To get conversion rates for a specific currency: BASE-URL/currency/YOUR-CURRENCY # currency/usd (case insensitive)  
- To get the result of converting one currency to another:  
    - BASE-URL/currency/convert/BASE-CURRENCY/TARGET-CURRENCY/QUANTITY  
    - BASE-URL/currency/convert/usd/aED/100 (case insensitive)  


## ЗАПУСК И РАБОТА
### Подготовительный этап
- Для запуска проекта нелбходимо установить Python (3.11 желательно)
- Через терминал в папке проекта настроить вертуальное окружение командой `python -m venv venv`
- Ввести команду `pip install -r src/requirements/prod.txt` для загрузки необходимых библиотек
- В файлу `.env` прописать параметры базы данных и подключения к API https://www.exchangerate-api.com/
- Далее для настройки необходимых таблиц в базе ввести команду `alembic revision --autogenerate -m "YOUR-DB-NAME"`
- Применить миграции alembic командой `alembic upgrade head`
- Проверить правильность работы введя команду из основной директории проекта `uvicorn src.main:app`
- После успешного запуска в тестовом режиме зайти в `src/config.py` и изменить переиенную `DEBUG = False`
- Запустить проект командой uvicorn `src.main:app`
- Подождать некоторое врямя для обновления базы данных

### Работа с API
- Для получения всех доступных для конвертации валют: BASE-URL/currency/supported
- Для получения всех кодов валют с коэфицентом конвертации: BASE-URL/currency/all
- Для полученяи коэфицентов конвертации конкретной валюты: BASE-URL/currency/YOUR-CURRENCY  #  currency/usd (регистр не имеет значения)
- Для получения результата конвертации одной валюты в другую:
    - BASE-URL/currency/convert/BASE-CURRENCY/TARGET-CURRENCY/QUANTITY
    - BASE-URL/currency/convert/usd/aED/100 (регистр не имеет значения)
