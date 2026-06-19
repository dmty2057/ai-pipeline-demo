"""Обробка платежів користувачів."""
from demo.users import get_user


def charge(user_id: int, amount: float) -> dict:
    """Списати кошти з користувача."""
    user = get_user(user_id)
    if user is None:
        return {"status": "failed", "reason": "unknown_user"}
    if not isinstance(amount, (int, float)):
        return {"status": "failed", "reason": "invalid_amount_type"}
    if amount <= 0:
        return {"status": "failed", "reason": "invalid_amount"}
    return {"status": "charged", "to": user.email, "amount": amount}


def refund(user_id: int, amount: float) -> dict:
    """Повернути кошти користувачу."""
    user = get_user(user_id)
    if user is None:
        return {"status": "failed", "reason": "unknown_user"}
    if amount <= 0:
        return {"status": "failed", "reason": "invalid_amount"}
    return {"status": "refunded", "to": user.email, "amount": amount}


def apply_late_fee(user_id: int, base_amount: float, days_overdue: int) -> dict:
    """Нарахувати пеню за прострочення."""
    user = get_user(user_id)
    if user is None:
        return {"status": "failed", "reason": "unknown_user"}
    if days_overdue <= 0:
        return {"status": "no_fee", "amount": base_amount}
    fee = base_amount * 0.1 * days_overdue
    total = round(base_amount + fee, 2)
    return {"status": "fee_applied", "to": user.email, "total": total}


def bulk_charge(user_ids: list, amount: float) -> dict:
    """Списати однакову суму з кількох користувачів (без тестів)."""
    results = {}
    for uid in user_ids:
        results[uid] = charge(uid, amount)
    ok = sum(1 for r in results.values() if r["status"] == "charged")
    return {"charged": ok, "total": len(user_ids), "results": results}
