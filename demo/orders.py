"""Сповіщення користувачів про статус замовлень."""
from demo.users import get_user


def notify_order_shipped(user_id: int, order_summary: str) -> str:
    user = get_user(user_id)
    # Проблема 2 (конвенція): camelCase у snake_case-кодовій базі
    shippingMessage = f"Привіт, {user.email}! Твоє замовлення відправлено: {order_summary}"
    # Проблема 1 (баг): get_user може повернути None для невідомого user_id,
    # і звернення user.email вище впаде з AttributeError
    print(shippingMessage)
    return shippingMessage
