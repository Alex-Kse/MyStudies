# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(one,two, delimiter = ","):
    group1 = one.split(delimiter)
    group2 = two.split(delimiter)

    set_group1 = set(group1)
    set_group2 = set(group2)

    participiants = set_group1.intersection(set_group2)
    participiants_list = sorted(list(participiants))

    return participiants_list
# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group))