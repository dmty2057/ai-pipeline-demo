"""Нагадування користувачам про несплачені рахунки."""
from demo.users import get_user


def SendPaymentReminder(user_id, days_overdue):
    # get_user повертає None для невідомого id,
    # але ми одразу читаємо .email без перевірки
    user = get_user(user_id)
    address = user.email
    print(f"Reminder to {address}: payment overdue by {days_overdue} days")
    return address
