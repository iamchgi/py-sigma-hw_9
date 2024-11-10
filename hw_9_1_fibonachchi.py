
'''

Послідовність чисел Фібоначчі має вираз Fn = Fn-1 + Fn-2: наступне число є сумою двох попередніх.
'''

# Python реалізація в рекурсівному обчислення ряду чисел Фібоначчі

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# перевірка валідності по кількості елементів
if nterms <= 0:
   print("Будь-ласка, задайте позитивне ціле")
else:
   print("обчислення ряду чисел Фібоначчі:")
   for i in range(nterms):
       print(recur_fibo(i))



