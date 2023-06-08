import pytest
from src.keyboard import KeyBoard

class TestKeyBoard:

    @pytest.fixture
    def keyboard(self):
        return KeyBoard('Redragon S101 Wired Rgb Backlit', 4600, 10, 'EN')

    # TestCase #1
    def test_language_valid(self):
        kb = KeyBoard('Redragon S101 Wired Rgb Backlit', 4600.0, 5)
        kb.change_lang()
        assert kb.language == 'RU'
        kb.change_lang()
        assert kb.language == 'EN'

    # TestCase #2
    def test_language_invalid(self):
        kb = KeyBoard('Redragon S101 Wired Rgb Backlit', 4600.0, 5)
        with pytest.raises(AttributeError):
            kb.language = 'CH'

    # TestCase #3
    def test_repr_(self, keyboard):
        assert repr(keyboard) == "KeyBoard('Redragon S101 Wired Rgb Backlit', 4600, 10, EN)"

    # TestCase #4
    def test_str_(self, keyboard):
        assert str(keyboard) == 'Redragon S101 Wired Rgb Backlit'

    # TestCase #5
    def test_cange_lang(self, keyboard):
        assert str(keyboard.language) == "EN"
        keyboard.change_lang()
        assert str(keyboard.language) == "RU"
        keyboard.change_lang().change_lang()
        assert str(keyboard.language) == "RU"




