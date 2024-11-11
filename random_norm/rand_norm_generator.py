"""
Скрипт файлу rand_norm_generator.py реалізує формування нормального закону розподілу випадкової величини,
як адитивна суміш двох рівномірних законів за принципами циклічних повторень. За допомогою функції генератора

Package Version
------- -------
pip         24.3.1
matplotlib  3.9.2
numpy       2.1.3

"""

import numpy as np
from math import sqrt, cos, log
import matplotlib.pyplot as plt


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


def generator_rand_norm(n):
    c = 2 * np.pi
    for i in range(n):
        values = np.random.rand(2)  # генерація рівномірних ВВ
        r = sqrt(-2 * log(values[0]))  # розраховуємо модель закону розподілу
        f = c * values[1]
        n_d = r * cos(f)  # нормальний розподіл за формулою norm = r*cos(f)
        yield values[0], values[1], n_d
    return


def rand_norm_generator_main() -> None:
    # задаємо параметри вибрики
    n = 10_000  # кількість елементів
    v1 = [] # рівномірний розподіл 1
    v2 = [] # рівномірний розподіл 2
    norm_dest = [] # нормальний розподіл

    for num in generator_rand_norm(n):
        v1.append(num[0])
        v2.append(num[1])
        norm_dest.append(num[2])

    # візуалізуємо Рівномірний розподіл
    uniform_distribution_draw(v1, v2)
    # будуємо гістограму
    histogram_show(norm_dest)
    return None
