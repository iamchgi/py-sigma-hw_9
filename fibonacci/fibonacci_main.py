"""
Виконав: Григорій Чернолуцький
Знаходження чисел Фібоначчі:
1.1. Шляхом створення ітератора – iterator;
1.2. Шляхом створення генераторної функції – generator function;
1.3. Шляхом створення генераторного виразу – generator expression.
Для порівняння з рекурсивним методом
Послідовність чисел Фібоначчі має вираз Fn = Fn-1 + Fn-2: наступне число є сумою двох попередніх.

Package Version
------- -------
pip 24.3.1

"""
from fibonacci.exp_fibonacci import fibonacci_exp_show
from fibonacci.generator_fibonacci import fibonacci_generator_show
from fibonacci.iter_fibonacci import fibonacci_iterator_show
from fibonacci.recur_fibonacci import fibonacci_recursion_show


def fibonacci_main(n) -> None:
    # перевірка валідності за кількістю елементів
    if n <= 0 or n > 35:
        print("Вхідні параметри хибні, корегую....")
        n = 35
    # реалізація обчислення ряду чисел Фібоначчі за допомогою функції-генератора
    fibonacci_generator_show(n)
    # реалізація обчислення ряду чисел Фібоначчі за допомогою генераторного виразу
    fibonacci_exp_show(n)
    # реалізація обчислення ряду чисел Фібоначчі за допомогою ітератора
    fibonacci_iterator_show(n)
    # реалізація в рекурсівному обчислення ряду чисел Фібоначчі
    fibonacci_recursion_show(n)
    return None
