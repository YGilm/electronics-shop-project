"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


class TestItem:

    def test_calculate_total_price(self):
        item = Item("item1", 15.0, 10)
        assert item.calculate_total_price() == 150.0

    def test_apply_discount(self):
        item = Item("item1", 10.0, 5)
        item.apply_discount()
        assert item.price == 10.0

    def test_all_items_list(self):
        item = Item("item1", 15.0, 10)
        assert item in Item.all
