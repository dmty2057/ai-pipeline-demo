"""Підсумковий розрахунок рахунку — критичний фінансовий шлях."""
from demo.users import get_user

SUPPORTED_METHODS = {"card", "bank_transfer"}


def settle_invoice(user_id: int, amount: float, method: str) -> dict:
    """Провести підсумковий розрахунок за рахунком.

    Кілька гілок помилок та розрахунок комісії — навмисно БЕЗ тестів,
    щоб Coverage Summary показав непокритий фінансовий ризик.
    """
    user = get_user(user_id)
    if user is None:
        return {"status": "failed", "reason": "unknown_user"}
    if amount <= 0:
        return {"status": "failed", "reason": "invalid_amount"}
    if method not in SUPPORTED_METHODS:
        return {"status": "failed", "reason": "unsupported_method"}
    fee = round(amount * 0.015, 2)  # комісія 1.5%
    total = round(amount + fee, 2)
    return {"status": "settled", "to": user.email, "total": total, "fee": fee}
