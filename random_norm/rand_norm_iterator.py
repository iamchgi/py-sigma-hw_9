"""
Скрипт файлу rand_norm_iterator.py реалізує формування нормального закону розподілу випадкової величини,
як адитивна суміш двох рівномірних законів за принципами циклічних повторень. За допомогою ітератора.

Package Version
------- -------
pip 24.3.1
matplotlib 3.9.2
numpy 2.1.3

"""

import numpy as np
from math import sqrt, cos, log
import matplotlib.pyplot as plt


class RandNormIterator:
    c = 2 * np.pi

    def __init__(self, n):
        self.index = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.max:
            raise StopIteration
        values = np.random.rand(2)
        r = sqrt(-2 * log(values[0]))
        f = self.c * values[1]
        n_d = r * cos(f)
        self.index += 1
        return values[0], values[1], n_d


def uniform_distribution_draw(v1, v2) -> None:
    print(f'Перший рівномірний розподіл: {v1[:20]}\nДругий рівномірний розподіл: {v2[:20]}')
    # візуалізуємо ВВ
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].hist(v1, bins=20)
    axes[1].hist(v2, bins=20)
    plt.show()
    return None


def histogram_show(norm_dest) -> None:
    # будуємо гістограму
    plt.hist(norm_dest, bins=15)
    plt.show()
    print('Нормальний розподіл: ', norm_dest[:20])
    return None


def rand_norm_iterator_main() -> None:
    v1 = []  # рівномірний розподіл 1
    v2 = []  # рівномірний розподіл 2
    norm_dest = []  # нормальний розподіл
    # задаємо параметри вибрики
    n = 10_000  # кількість елементів
    rand_norm_iterator = RandNormIterator(n)
    for num in rand_norm_iterator:
        v1.append(num[0])
        v2.append(num[1])
        norm_dest.append(num[2])
    # візуалізуємо Рівномірний розподіл
    uniform_distribution_draw(v1, v2)
    # будуємо гістограму
    histogram_show(norm_dest)
    return None
