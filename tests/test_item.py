"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item, CSV_PATH


class TestItem:

    # TestCase #1 calculate_total_price
    def test_calculate_total_price(self):
        item = Item("item1", 15.0, 10)
        assert item.calculate_total_price() == 150.0

    # TestCase #2 apply_discount
    def test_apply_discount(self):
        item = Item("item1", 10.0, 5)
        item.apply_discount()
        assert item.price == 10.0

    # TestCase #3 all_items_list
    def test_all_items_list(self):
        item = Item("item1", 15.0, 10)
        assert item in Item.all

    # TestCase #4 name getter
    def test_name(self):
        item3 = Item('samsung galaxy', 0.0, 0)
        assert item3.name == 'samsung galaxy'

    # TestCase #5 name setter
    def test_set_name(self):
        item2 = Item('iphone x', 0.0, 0)
        item2.name = 'iphone x'
        assert item2.name == 'iphone x'

    # TestCase #6  name setter
    def test_set_name_exceeds_limit(self):
        item = Item('samsung galaxy', 0.0, 0)
        try:
            item.name = 'Длинное наименование'
        except ValueError as e:
            assert str(e) == 'Длина имени не должна превышать 10 символов.'


    # TestCase #7
    def test_instantiate_from_csv(self):

        # Вызываем метод instantiate_from_csv
        items = Item.instantiate_from_csv(CSV_PATH)

        # Проверяем результат
        assert len(items) == 5

        # Проверяем значения для каждого элемента
        assert items[0].name == 'Смартфон'
        assert items[0].price == 100
        assert items[0].quantity == 1

        assert items[1].name == 'Ноутбук'
        assert items[1].price == 1000
        assert items[1].quantity == 3

    # TestCase #8
    def test_string_to_number(self):
        assert Item.string_to_number("123") == 123
        assert Item.string_to_number("-456") == -456
        assert Item.string_to_number("3.14") == 3
        with pytest.raises(ValueError) as value_info:
            Item.string_to_number("abc")

        assert str(value_info.value) == "Не является числом"

    # TestCase #9
    def test_repr_(self):
        item1 = Item('Samsung S21', 70000, 15)
        assert repr(item1) == "Item('Samsung S21', 70000, 15)"

    # TestCase #10
    def test_str_(self):
        item1 = Item('Samsung S21', 70000, 15)
        assert str(item1) == 'Samsung S21'

    # TestCase #11
    def test_addition(self):
        from src.phone import Phone
        phone = Phone('Iphone 13', 100000, 10, 2)
        ithem = Item('Samsung Galaxy S22', 80000, 15)
        total = phone + ithem
        assert total == 25

    # TestCase #12
    def test_add_invalid_type(self):
        from src.phone import Phone
        phone1 = Phone("iphone 13", 100000, 5, 2)
        invalid_obj = "Недопустимый объект"

        with pytest.raises(TypeError):  # Проверяем, что при сложении с недопустимым типом вызывается исключение
            phone1 + invalid_obj
