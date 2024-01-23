"""Завдання 2"""

import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    if not (1 <= min <= quantity <= max <= 1000):
        print("Неправильні параметри")
        return []
    empty_set = set()
    while len(empty_set) < quantity:
        empty_set.add(random.randint(min, max))
    result = sorted(list(empty_set))
    return result


lottery_numbers = get_numbers_ticket(1, 45, 6)
print(lottery_numbers)
