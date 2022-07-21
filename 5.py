# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



spisok_1 = [] 
n= int(input('Введите число => '))
fn1 = 1
fn2 = -1
i = 0
spisok_1.append(fn1)
spisok_1.append(fn2)
while i < n-2:
    fsum = fn1 - fn2
    fn1 = fn2
    fn2 = fsum
    i += 1
    spisok_1.append(fsum)
list.reverse(spisok_1)

fnn1 = 0
fnn2 = 1
i = 0
spisok_1.append(fnn1)
spisok_1.append(fnn2)
while i < n-1:
    fsum2 = fnn1 + fnn2
    fnn1 = fnn2
    fnn2 = fsum2
    i += 1
    spisok_1.append(fsum2)
print(spisok_1)