from src.item import Item


class MixinLanguage:
    """
    Класс-миксин для обеспечения функциональности языка.
    """
    def __init__(self, language='EN'):
        """
        Инициализация объекта MixinLanguage.
        Аргументы: language (str): Код языка. По умолчанию 'EN'.
        """
        self._MixinLanguage__language = language

    @property
    def language(self):
        """
        Получить текущий язык клавиатуры.
        Возвращает: str: Код текущего языка клавиатуры.
        """
        return self._MixinLanguage__language

    def change_lang(self):
        """
        Изменить язык клавиатуры между 'EN' и 'RU'.
        """
        if self._MixinLanguage__language == 'EN':
            self._MixinLanguage__language = 'RU'
        else:
            self._MixinLanguage__language = 'EN'
        return self


class KeyBoard(Item, MixinLanguage):
    """
    Класс, представляющий клавиатуру.
    """
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        """
        Инициализация объекта KeyBoard.
        Аргументы:
            name (str): Название клавиатуры.
            price (float): Цена клавиатуры.
            quantity (int): Количество клавиатур.
            language (str): Код языка. По умолчанию 'EN'.
        """
        super().__init__(name, price, quantity)
        self._MixinLanguage__language = language

    def __repr__(self):
        """
        Получить строковое представление объекта KeyBoard.
        Возвращает: str: Строковое представление объекта KeyBoard.
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    def __str__(self):
        """
        Получить строковое представление объекта KeyBoard.
        Возвращает: str: Строковое представление объекта KeyBoard.
        """
        return f"{self.name}"
