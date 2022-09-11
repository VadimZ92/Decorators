from datetime import datetime
from pprint import pprint
import os

datetime = datetime.now()

def Param_Decorator(path):

    def Decorator(old_func):

        def new_func(*args, **kwargs):
            print()
            print(f'Функция вызвана {datetime}')
            print(f'Название функции: "{old_func.__name__}"')
            print(f'С аргументами: {args} и {kwargs}')
            result = old_func(*args, **kwargs)
            pprint(f'Результат работы функции "{old_func.__name__}" : {result}')
            print()
            with open(path, "a", encoding="utf-8") as file:
                file.write(f"...\n"
                           f"  Функция вызвана {datetime}\n "
                           f" Название функции: '{old_func.__name__}'\n "
                           f" С аргументами: {args} и {kwargs}\n "
                           f" Результат работы функции '{old_func.__name__}' : {result}\n ")
            return result
        return new_func
    return Decorator
