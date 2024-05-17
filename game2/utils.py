import random

def calculate_exhaustion(distance):
    return max(0, distance // 10 - 1)

def generate_random_event():
    return random.choice(["nothing", "found_food", "found_weapon", "found_animal"])

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)
