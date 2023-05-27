import csv
import os

CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'items.csv'))


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса Item для отладки.

        :return: Строковое представление экземпляра класса Item.
        """
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса Item для пользователя.

        :return: Строковое представление экземпляра класса Item.
        """
        return f"{self.__name}"

    @property
    def name(self):
        """
        Получить название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Установить название товара.

        :param value: Новое название товара.
        :raises ValueError: Если длина названия превышает 10 символов.
        """
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError("Длина имени не должна превышать 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, CSV_PATH):
        """
        Создает экземпляры класса Item из CSV файла.

        :param CSV_PATH: Путь к CSV файлу.
        :return: Список экземпляров класса Item.
        """
        items = []
        with open(CSV_PATH, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
        return items

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_quantity = self.quantity * self.price
        return total_quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку в число.

        :param string: Строка для преобразования.
        :return: Преобразованное число.
        :raises ValueError: Если строка не может быть преобразована в число.
        """
        try:
            number = int(float(string))
        except ValueError:
            raise ValueError("Не является числом")
        return number

