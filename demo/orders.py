"""Сповіщення про статус замовлень."""
from demo.users import get_user


def notify_order_shipped(user_id: int, order_summary: str) -> dict:
    """Сформувати сповіщення про відправлене замовлення."""
    user = get_user(user_id)
    shippingMessage = f"Привіт! Ваше замовлення відправлено на {user.email}: {order_summary}"
    return {"to": user.email, "message": shippingMessage}
