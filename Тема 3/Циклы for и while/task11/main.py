num = 123
count = 0
while num > 1:
    num = (num * 3 + 1) / 2 if num % 2 else num / 2
    count += 1
# TODO посчитать количество действий над числом согласно условию

print(count)
