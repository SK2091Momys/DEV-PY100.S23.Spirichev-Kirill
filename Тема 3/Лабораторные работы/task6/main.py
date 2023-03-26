list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number = 0
index_max = 0
for i in list_numbers:
    if i > max_number:
        max_number = i
        index_max = list_numbers.index(max_number)
list_numbers[index_max], list_numbers[len(list_numbers) - 1] = list_numbers[len(list_numbers) - 1], list_numbers[index_max]
# TODO Оформить решение
# Второй вариант:
# list_numbers[list_numbers.index(max(list_numbers))], list_numbers[len(list_numbers) - 1] = list_numbers[len(list_numbers) - 1], list_numbers[list_numbers.index(max(list_numbers))]
print(list_numbers)
