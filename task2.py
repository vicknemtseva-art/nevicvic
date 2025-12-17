
# Исходные данные
salary = 5000  # ежемесячная зарплата
spend = 6000  # траты за первый месяц
increase = 0.03  # ежемесячный рост цен (3%)
month_target = 10  # количество месяцев, которое нужно протянуть
money_capital = 0
for month in range(month_target):
    current_spend = spend * (1 + increase) ** month
    deficit = current_spend - salary
    money_capital += deficit
money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {month_target} месяцев без долгов:", money_capital)