# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    texts =""
    slov ={}
    for i in text:
        if i.isalpha() == True:
            texts+= i
        else:
            continue
    for i in texts:
        if i in slov:
            slov[i] += 1
        else:
            slov[i] = 1
    return slov

# TODO Напишите функцию calculate_frequency
def calculate_frequency(x):
    summ=0
    for i in x:
        summ+= x[i]
    for i in x:
        cof = x[i]/summ
        print(f"{i}: {cof:.2f}")


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
calculate_frequency(count_letters(main_str))