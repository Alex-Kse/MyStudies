salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
months = 10
allmoney = 0
month = 0
for i in range(1, months + 1):
    allmoney += salary
    month += 1
    if month == 1:
        spend = spend

    else:
        spend = spend + (spend * increase)

    allmoney -= spend

allmoney *= -1
allmoney = round(allmoney, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", allmoney)