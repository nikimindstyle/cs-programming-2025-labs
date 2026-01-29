import random
def create_character():
    print("Выберите расу:")
    print("1 - Человек")
    print("2 - Эльф")
    print("3 - Дворф")
    while True:
        try:
            choice = int(input("> "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Введите 1, 2 или 3.")
        except ValueError:
            print("Пожалуйста, введите число.")

# после распределения характеристик
    character = {
        "name": "Герой","race": race_name,
        "level": 1, "exp": 0, "exp_to_next": 100,
        "hp": hp, "max_hp": hp, "base_attack": attack,
        "base_defense": defense,
        "agility": agility, "weapon_level": 0,
        "armor_level": 0,
        "inventory": {"health_potions": 1,"coins": 50}
    }
    return character