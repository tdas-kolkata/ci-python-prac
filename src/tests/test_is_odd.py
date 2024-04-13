from src.app.main import is_odd, is_even

def test_is_odd_for_odds():
    assert is_odd(3) == True

def test_is_odd_for_even():
    assert is_odd(2) == False

def test_is_even_for_odds():
    assert is_even(3) == False
    
def test_is_even_for_even():
    assert is_even(2) == True