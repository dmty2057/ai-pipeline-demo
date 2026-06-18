"""Простий шар доступу до користувачів для демо."""
from typing import Optional


class User:
    def __init__(self, user_id: int, email: str) -> None:
        self.user_id = user_id
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.user_id}, email={self.email!r})"


# Імітація "бази": не кожен id існує.
_USERS = {
    1: User(1, "alice@example.com"),
    2: User(2, "bob@example.com"),
}


def get_user(user_id: int) -> Optional[User]:
    """Повертає User або None, якщо користувача не знайдено."""
    return _USERS.get(user_id)


def list_active_users() -> list:
    """Повернути список усіх відомих користувачів."""
    return list(_USERS.values())
