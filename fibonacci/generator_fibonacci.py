
# функція-генератор для реалізації обчислення ряду чисел Фібоначчі

def generator_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_generator_show(n) -> None:
    my_gen = generator_fibonacci(n)
    print("Обчислення ряду чисел Фібоначчі:")
    for i in my_gen:
        print(i, end=" ")
    print(" ")
    return