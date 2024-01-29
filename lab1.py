class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        if not isinstance(pages,int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self.pages = pages




class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        if not isinstance(duration,(float,int)):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self.duration = duration
