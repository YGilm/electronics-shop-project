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
        self.__language = language


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
        self.__language = language

    @property
    def language(self):
        """
        Получить текущий язык клавиатуры.
        Возвращает: str: Код текущего языка клавиатуры.
        """
        return self.__language

    @language.setter
    def language(self, value):
        """
        Установить язык клавиатуры.
        Аргументы: value (str): Код языка.
        Исключения: AttributeError: Если код языка не поддерживается.
        """
        if value in ['EN', 'RU']:
            self.__language = value
        else:
            raise AttributeError("Данный язык не поддерживается")

    def change_lang(self):
        """
        Изменить язык клавиатуры между 'EN' и 'RU'.
        Возвращает: KeyBoard: Обновленный объект KeyBoard.
        """
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

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
