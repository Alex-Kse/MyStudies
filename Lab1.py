# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Phone:
    def __init__(self, weight: (int, float), diagonal: (int, float), price: (int, float)):
        """
        :param weight: Вес телефона
        :param diagonal: Диагональ экрана телефона
        :param price: Цена телефона
        Так же проверяется чтобы каждое введенное значение было int или float
        Примеры:
        >>> myphone = Phone(200,6.6,850)
        """
        if weight < 150:
            raise ValueError
        if not isinstance(weight, (int, float)):
            raise TypeError
        self.weight = weight
        if diagonal < 5:
            raise ValueError
        if not isinstance(diagonal, (int, float)):
            raise TypeError
        self.diagonal = diagonal
        if price < 100:
            raise ValueError
        if not isinstance(price, (int, float)):
            raise TypeError
        self.price = price

    def highcost(self):
        """
        Функция проверяет является ли телефон дорогим
        :return: Дорогой телефон или приемлемый
        Пример:
        >>> one = Phone(200,6.5,800)
        >>> one.highcost()
        Дорого
        """
        if self.price > 700:
            print("Дорого")
        else:
            print("Приемлемо")
    def miniphone(self):
        """
        Функция проверяет стандартного размера телефон или мини
        :return: Mini phone or Normal phone
        Пример:
        >>> one = Phone(200,6.5,800)
        >>> one.miniphone()
        Normal phone
        """
        if self.diagonal < 6 :
            print("Mini phone")
        else:
            print("Normal phone")

class Guitars:
    """
    Создание и подготовка к работе с Гитара
    :strings: Количество струн
    :body: Количество корпусов
    """
    def __init__(self,strings,body):
        if strings < 6 :
            raise ValueError
        if not isinstance(strings, int):
            raise TypeError
        self.strings = strings
        if body < 1:
            raise ValueError
        if not isinstance(strings, int):
            raise TypeError
        self.body = body

    def assembling(self)->bool:
        """
        Функция проверяющая можно ли собрать одну гитару
        Пример:
        >>> guitar = Guitars(7,2)
        >>> guitar.assembling()
        """
        ...
    def nonassebml(self)->bool:
        """
        Функция проверяющаяя чего не хватает для сборки одной гитары
        >>> guitar = Guitars(7,2)
        >>> guitar.nonassebml()
        """
        ...
class Tea:
    """
    Создание и подготовка к работе с  чай
    :hotwater: Количество воды для чая
    :tea: Заварка

    """
    def __init__(self,hotwater,tea):
        if hotwater <50 :
            raise ValueError
        if not isinstance(hotwater, (int,float)):
            raise TypeError
        self.tea = tea
        if tea < 1:
            raise ValueError
        if not isinstance(tea, int):
            raise TypeError
        self.tea = tea
    def maketea(self)->bool:
        """
        Проверяет если ли у нас всё для чая
        >>> tea = Tea(60,2)
        >>> tea.maketea()
        """
        ...
    def notea(self)->bool:
        """
        Проверяет чего не хватает для чая
        >>> tea = Tea(60,2)
        >>> tea.notea()
        """
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
