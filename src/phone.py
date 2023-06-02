from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Конструктор класса Phone.
        Параметры:
        name (str): Название телефона.
        price (float): Цена телефона.
        quantity (int): Количество товара в магазине.
        number_of_sim (int): Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = None
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Переопределяем метод __repr__ добовляем атрибут класса number_of_sim.
        Возвращает: str: Строковое представление экземпляра класса для отладки.
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает: int: Количество поддерживаемых сим-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
       """
       Устанавливает колличество поддерживаемых сим-карт.
       Параметры: value (int): Количество поддерживаемых сим-карт.
       raises: ValueError: Если значение не больше нуля.
       """
       if not isinstance(value, int) or value > 0:
           self.__number_of_sim = value
       else:
           raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


