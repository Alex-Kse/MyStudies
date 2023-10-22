salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
months = 10
money = 0
for i in range(1, months + 1):
    money += salary-spend
    spend = spend + (spend * increase)

money *= -1
money = round(money, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money)