"""Тести кодують бізнес-правила для платежів.
Частина навмисно червоні — правила ще не реалізовані в коді."""
from demo.payments import refund, apply_late_fee


def test_refund_known_user_ok():
    result = refund(1, 50)
    assert result["status"] == "refunded"


def test_refund_unknown_user_rejected():
    result = refund(999, 50)
    assert result["status"] == "failed"


def test_refund_returns_transaction_id():
    # Бізнес-вимога: кожне повернення має містити transaction_id (ще не реалізовано).
    result = refund(1, 50)
    assert "transaction_id" in result


def test_late_fee_capped_at_50_percent():
    # Бізнес-правило: пеня не може перевищувати 50% базової суми (ще не реалізовано).
    result = apply_late_fee(1, 100, 10)  # fee = 100 -> total 200
    assert result["total"] <= 150
