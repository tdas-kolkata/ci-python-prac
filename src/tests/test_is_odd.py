from src.app.main import is_odd

def test_is_odd_for_odds():
    assert is_odd(3) == True

def test_is_odd_for_even():
    assert is_odd(2) == False