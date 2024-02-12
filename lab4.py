if __name__ == "__main__":

    class Animals:
        """Класс Animals для записи животных с параметрами возраста и имени"""
        def __init__(self, age: int, name: str):
            """Вызываем конструктор класса"""
            self._age = age
            self._name = name

        def __str__(self) -> str:
            """Магический метод возвращающий неформальное строковое представление объекта"""
            return f"Животное{self._name}, его возраст {self._age}"

        def __repr__(self) -> str:
            """Магический метод возвращающий валидную строку, может быть использованно для воссоздания объекта"""
            return f"{self.__class__.__name__}(age={self._age!r},name={self._name!r})"

        def info(self) -> str:
            """Метод дающий общую информацию о животном"""
            return f"Имя животного:{self._name}, его возраст:{self._age}"


        @property
        def age(self) -> int:
            """Защищаем переменную age  от перезаписи"""
            return self._age

        @property
        def name(self) -> str:
            """Защищаем переменную name  от перезаписи"""
            return self._name

    class Herbivores(Animals):
        """Унаследованный класс Herbivores от Animals добовляет к уже
        введенным параметрам параметр пищи, в данном подклассе
        должны указываться травоядные.(Параметр food просто конкретезирует
        что именно они едят:траву, листья, древесину(термиты))"""
        def __init__(self, age: int, name: str, food: str):
            super().__init__(age, name)
            self._food = food
            self.info()

        @property
        def food(self) -> str:
            """Защищаем переменную food от перезаписи"""
            return self._food

        def __str__(self) -> str:
            """Перегружаем магический метод из-за нового параметра еды"""
            return f"Животное{self._name}, его возраст {self._age}, еда :{self._food}"

        def __repr__(self) -> str:
            """Перегружаем магический метод из-за нового параметра еды"""
            return f"{self.__class__.__name__}(age={self._age!r},name={self._name!r},food={self._food!r})"


    pass
