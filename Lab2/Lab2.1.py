money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
allmoney = money_capital
month = 0

while allmoney >= 0:
    allmoney += salary
    spend = spend + (spend * increase)
    allmoney -= spend
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
