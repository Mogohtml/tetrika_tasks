"""
Задание 1: Необходимо реализовать декоратор @strict
Декоратор проверяет соответствие типов переданных
в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
(подсказка: аннотации типов аргументов можно получить из атрибута объекта
функции func.__annotations__ или с помощью модуля inspect)
При несоответствии типов бросать исключение TypeError Гарантируется, что параметры
в декорируемых функциях будут следующих типов: bool, int, float, str Гарантируется,
что в декорируемых функциях не будет значений параметров, заданных по умолчанию
"""

def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for arg, arg_type in zip(args, annotations.values()):
            if not isinstance(arg, arg_type):
                raise TypeError(f"Argument {arg} is not of type {arg_type}")
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(sum_two(1, 2))  # -- 3
    try:
        print(sum_two(1, 2.4))  # -- TypeError
    except TypeError as e:
        print(e)
