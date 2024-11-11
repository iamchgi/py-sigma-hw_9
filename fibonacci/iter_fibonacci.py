# Клас для реалізації обчислення ряду чисел Фібоначчі за допомогою ітератора

class Fibonacci:
    last = 0
    current = 1

    def __init__(self, n):
        self.index = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.max:
            raise StopIteration

        result = self.last
        self.last, self.current = self.current, self.last + self.current
        self.index += 1
        return result

def fibonacci_iterator_show(n) -> None:
    fib_iter = Fibonacci(n)
    for i in fib_iter:
        print(i, end=" ")
    print("")
    return