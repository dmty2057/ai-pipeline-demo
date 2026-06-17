"""Надсилання сповіщень користувачам."""
from demo.users import get_user


def SendWelcomeEmail(user_id):
    # get_user може повернути None, якщо користувача немає,
    # але ми одразу звертаємось до .email
    user = get_user(user_id)
    address = user.email
    print(f"Sending welcome email to {address}")
    return address
