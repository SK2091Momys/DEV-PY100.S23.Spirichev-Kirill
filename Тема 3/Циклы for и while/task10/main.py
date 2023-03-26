list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]
count_even_number = 0
count_odd_number = 0
for number in list_:
    if number // 2:
        count_even_number += 1
    else:
        count_odd_number += 1
if count_even_number < count_odd_number:
    print("Нечетных чисел больше")
elif count_odd_number < count_even_number:
    print("Четных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")

# TODO завести отдельные счетчики для четных и нечетных чисел

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

# TODO вывести каких чисел больше
