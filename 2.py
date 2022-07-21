# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

spisok_1 = [2, 5, 1, 3, 8, 4, 5]
spisok_2 = []
for i in range(len(spisok_1) // 2):
    c = spisok_1[i] * spisok_1[-i-1]
    spisok_2.append(c)
if len(spisok_1) % 2 > 0:
    d = (len(spisok_1) // 2)
    d = spisok_1[d] ** 2
    spisok_2.append(d)   
print(spisok_2) 

