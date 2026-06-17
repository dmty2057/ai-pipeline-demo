"""Простий шар доступу до користувачів для демо."""
from typing import Optional


class User:
    def __init__(self, user_id: int, email: str) -> None:
        self.user_id = user_id
        self.email = email


# Імітація "бази": не кожен id існує.
_USERS = {
    1: User(1, "alice@example.com"),
    2: User(2, "bob@example.com"),
}


def get_user(user_id: int) -> Optional[User]:
    """Повертає User або None, якщо користувача не знайдено."""
    return _USERS.get(user_id)
