"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""

def function(**kwargs) -> dict:
    return {v if v.__hash__ is not None else str(v):k for k,v in kwargs.items()}
            

if __name__ == '__main__': 
    print(function(argument1 = 999, argument2 = "string", argument3 = "999", argument4 = [1,2,3,4,5], argument5 = 2.3, argument6 = {1,2,3,4,5}))
