import pytest
from src.cinema_price import ticket_price

def test_price_valid_value():
    assert ticket_price(0) == 0
    assert ticket_price(1) == 1200
    assert ticket_price(2) == 2400
    assert ticket_price(3) == 3600

@pytest.mark.parametrize(
    "ticket_count",
    [
        ("Number"), #Not an integer
        (-1), #Negative number
        (1.5), #Float (no decimals allowed)
    ],
)

def test_price(ticket_count):
    with pytest.raises((TypeError, ValueError)):
        ticket_price(ticket_count)