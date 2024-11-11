from itertools import islice, accumulate
import operator

# Генераторное выражение для чисел Фибоначчи
fibonacci_gen = accumulate([0, 1] + [0] * 8, lambda x, _: x + (x if _ % 2 else 1))

# Печать первых 10 чисел Фибоначчи
for num in islice(fibonacci_gen, 10):
    print(num)

# цей скрипт схожий на сову і глобус
