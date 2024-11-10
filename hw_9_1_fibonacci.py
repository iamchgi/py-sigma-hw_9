"""

Послідовність чисел Фібоначчі має вираз Fn = Fn-1 + Fn-2: наступне число є сумою двох попередніх.
"""


# Python реалізація в рекурсівному обчислення ряду чисел Фібоначчі

def recur_fibo(n) -> int:
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


def my_generator_fibo(n):  # генератор для обчислення чисел Фібоначчі
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci(n) -> None:
    # перевірка валідності за кількістю елементів
    if n <= 0 or n > 35:
        print("Вхідні параметри хибні, корегую....")
        n = 35

    my_gen = my_generator_fibo(n)
    print("Обчислення ряду чисел Фібоначчі:")
    for i in my_gen:
        print(i, end=" ")
    print(" ")
    for i in range(n):
        print(recur_fibo(i), end=" ")
    print(" ")

    return None
