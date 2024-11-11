# реалізація обчислення ряду чисел Фібоначчі за допомогою генераторного виразу,
# але сумнівна ефективність цього методу !!!!!!!

def fibonacci_exp_show(n) -> None:
    n_2 = 0
    n_1 = 1
    generator_expr = (i for i in range(n))
    for _ in generator_expr:
        print(n_2, end=" ")
        n_2, n_1 = n_1, n_2 + n_1
    print("")
    return
