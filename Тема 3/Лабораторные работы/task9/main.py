salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0
for i in range(1,months+1):
    need_money += (spend - salary)  # количество денег, чтобы прожить 10 месяцев
    spend += increase * spend
# TODO Оформить решение

print(round(need_money))
