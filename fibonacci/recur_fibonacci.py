
#  Метод для реалізації в рекурсівному обчисленні ряду чисел Фібоначчі

def recur_fibonacci(n) -> int:
    if n <= 1:
        return n
    else:
        return (recur_fibonacci(n - 1) + recur_fibonacci(n - 2))

def fibonacci_recursion_show(n):
    for i in range(n):
        print(recur_fibonacci(i), end=" ")
    print(" ")
