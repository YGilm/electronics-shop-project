import pytest

from src.phone import Phone


class TestPhone:

    # TestCase #1
    @pytest.fixture
    def phone(self):
        return Phone("iPhone 14", 100000, 7, 2)

    # TestCase #2 __repr__
    def test_repr_(self, phone):
        assert repr(phone) == "Phone('iPhone 14', 100000, 7, 2)"

    # TestCase #3 number_of_sim_valid
    def test_number_of_sim_valid(self, phone):
        phone.number_of_sim = 3
        assert phone.number_of_sim == 3


    # TestCase #4 number_of_sim_invalid
    def test_number_of_sim_invalid(self, phone):
        with pytest.raises(ValueError):
            phone.number_of_sim = 0