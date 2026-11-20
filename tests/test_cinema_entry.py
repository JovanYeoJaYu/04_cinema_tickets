import pytest
from src.cinema_entry import can_watch

def test_can_watch_valid_value():
    assert can_watch(17) == True
    assert can_watch(16) == True
    assert can_watch(15) == False
    

@pytest.mark.parametrize(
    "age",
    [
        ("Number"), #Not an integer
        (-1), #Negative number
    ],
)
def test_can_watch(age):
    with pytest.raises((TypeError, ValueError)):
        can_watch(age)