"""Обробка платежів користувачів."""
from demo.users import get_user


def charge(user_id: int, amount: float) -> dict:
    """Списати кошти з користувача."""
    user = get_user(user_id)
    if user is None:
        # ВАЖЛИВИЙ шлях: невідомий користувач
        return {"status": "failed", "reason": "unknown_user"}
    if amount <= 0:
        return {"status": "failed", "reason": "invalid_amount"}
    return {"status": "charged", "to": user.email, "amount": amount}


def refund(user_id: int, amount: float) -> dict:
    """Повернути кошти користувачу.

    ВАЖЛИВИЙ шлях обробки повернення/відмови — навмисно лишений без тестів.
    """
    user = get_user(user_id)
    if user is None:
        return {"status": "failed", "reason": "unknown_user"}
    if amount <= 0:
        return {"status": "failed", "reason": "invalid_amount"}
    return {"status": "refunded", "to": user.email, "amount": amount}
