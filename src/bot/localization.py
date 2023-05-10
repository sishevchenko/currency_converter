start = {
    "ru": "Привет! Я - бот конвертор валют!\n"
          "Я умею:\n"
          "  - Конвертировать одну валюту в другую\n"
          "  - Показывать все поддерживаемые для конвертации валюты\n"
          "  - Показывать отношения указанной валюты к поддерживаемым\n"
          "  - и еще немножко ;)\n\n"
          "Инструкция:\n"
          "- Для полученя списка поддерживаемых валют в формате \"код_валюты назание_валюты\"\n"
          "    --> /supported"
          "- Для полученя соотношения указанной валюты к поддерживаемым\n"
          "    --> /rates код_валюты\n"
          "- Для конвертации одной валюты в другую\n"
          "    --> /covert код_валюты_1 код_валюты_2 колличество_валюты_1\n"
          "- Для получения информации по использованию\n"
          "    --> /help",
    "en": "Hi! I'm a currency converter bot!\n"
          "I can:\n"
          "- Convert one currency to another\n"
          " - Show all supported currencies for conversion\n"
          " - Show ratios of the specified currency to supported ones\n"
          "- and a little more ;)\n\n"
          "Instruction:\n"
          "- To get a list of supported currencies in the format \"currency_code currency_name\"\n"
          " --> /supported"
          "- To get the ratio of the specified currency to the supported ones\n"
          " --> /rates currency_code\n"
          "- To convert one currency to another\n"
          " --> /covert currency_code_1 currency_code_2 amount_currency_1\n"
          "- For usage information\n"
          " --> /help"
}

help = {
    "ru": "Я умею:\n"
          "  - Конвертировать одну валюту в другую\n"
          "  - Показывать все поддерживаемые для конвертации валюты\n"
          "  - Показывать отношения указанной валюты к поддерживаемым\n"
          "  - и еще немножко ;)\n\n"
          "Инструкция:\n"
          "- Для полученя списка поддерживаемых валют в формате \"код_валюты назание_валюты\"\n"
          "    --> /supported"
          "- Для полученя соотношения указанной валюты к поддерживаемым\n"
          "    --> /rates код_валюты\n"
          "- Для конвертации одной валюты в другую\n"
          "    --> /covert код_валюты_1 код_валюты_2 колличество_валюты_1\n",
    "en": "I can:\n"
          "- Convert one currency to another\n"
          " - Show all supported currencies for conversion\n"
          " - Show ratios of the specified currency to supported ones\n"
          "- and a little more ;)\n\n"
          "Instruction:\n"
          "- To get a list of supported currencies in the format \"currency_code currency_name\"\n"
          " --> /supported"
          "- To get the ratio of the specified currency to the supported ones\n"
          " --> /rates currency_code\n"
          "- To convert one currency to another\n"
          " --> /covert currency_code_1 currency_code_2 amount_currency_1\n"
}

conversion_state = {
    "ru": "Введите:\n"
          "код_валюты_1 код_валюты_2 колличество_валюты_1",
    "en": "Enter:\n"
          "currency code _1 currency code_2 currency amount _1"
}

rates_state = {
    "ru": "Введите:\n"
          "код_валюты",
    "en": "Enter:\n"
          "currency code"
}

errors = {
    "ru": "",
    "en": ""
}

language = {
    "help": help,
    "start": start,
    "conversion_state": conversion_state,
    "rates_state": rates_state,
    "errors": errors,
}
