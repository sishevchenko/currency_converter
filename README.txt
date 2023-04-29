The goal of the project is to develop an API for currency conversion using FastAPI and SQLAlchemy.
The API should provide the ability to get up-to-date exchange rates and convert between them.

Stages:

1. Getting current exchange rates:
    - Create a model for storing information about the currency (name, code, rate).
    - Implement a function that will request current exchange rates from an external API and store them in the database.

2. Conversion between currencies:
    - Implement a function that will accept two currencies as input (source and target) and the amount to be converted.
    - The function should return the conversion result based on the current exchange rates from the database.

3. Creating and configuring API:
    - Using FastAPI, create an API with two endpoints: one for getting current exchange rates, the other for converting between currencies.
    - Set up interaction with the database using SQLAlchemy.