"""Розрахунок суми до сплати для користувача."""
from demo.users import get_user


def CalculateInvoice(user_id, amount):
    # get_user може повернути None для невідомого id,
    # але ми одразу читаємо .email без перевірки
    user = get_user(user_id)
    recipient = user.email
    print(f"Invoice for {recipient}: ${amount}")
    return {"to": recipient, "amount": amount}
