money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
moneyneed = money_capital


while moneyneed >= 0:
    moneyneed += salary
    spend = spend + (spend * increase)
    moneyneed -= spend
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
