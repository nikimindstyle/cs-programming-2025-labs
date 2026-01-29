import random

def create_enemy(floor=1):
    enemy = {
        "name": random.choice(["Гоблин", "Скелет", "Орк", "Тролль", "Крыса"]),
        "hp": random.randint(20, 40),
        "max_hp": 0,
        "attack": random.randint(5, 10),
        "defense": random.randint(2, 6),
    }
    enemy["max_hp"] = enemy["hp"]
    return enemy

def create_mimic():
    """Создаёт мимика — усиленного врага"""
    base = create_enemy()
    mimic = {
        "name": "Мимик!",
        "hp": base["hp"] * 2,
        "max_hp": base["hp"] * 2,
        "attack": int(base["attack"] * 1.5),
        "defense": base["defense"],
    }
    return mimic