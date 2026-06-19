"""Тести покривають лише успішний шлях charge()."""
from demo.payments import charge


def test_charge_known_user():
    result = charge(1, 100)
    assert result["status"] == "charged"
    assert result["to"] == "alice@example.com"
    assert result["amount"] == 100


from demo.payments import charge_by_email
from demo.users import find_user_by_email


def test_find_user_by_email_known():
    user = find_user_by_email("alice@example.com")
    assert user is not None
    assert user.user_id == 1


def test_charge_by_email_known():
    result = charge_by_email("bob@example.com", 50)
    assert result["status"] == "charged"
    assert result["amount"] == 50
