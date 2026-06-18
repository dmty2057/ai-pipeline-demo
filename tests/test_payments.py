"""Тести покривають лише успішний шлях charge()."""
from demo.payments import charge


def test_charge_known_user():
    result = charge(1, 100)
    assert result["status"] == "charged"
    assert result["to"] == "alice@example.com"
    assert result["amount"] == 100
