# Исходные данные
money_capital = 20000  # финансовая подушка безопасности
salary = 5000  # ежемесячная зарплата
spend = 6000  # расходы в первый месяц
increase = 0.05  # ежемесячный рост цен

month = 0
current_capital = money_capital

while True:
    if month == 0:
        current_spend = spend
    else:
        current_spend = spend * (1 + increase) ** month
    current_budget = salary + current_capital
    if current_spend > current_budget:
        break
    current_capital = current_capital - (current_spend - salary)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)