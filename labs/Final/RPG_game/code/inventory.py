def get_total_attack(player):
    weapon_bonus = {0: 0, 1: 3, 2: 6, 3: 10}
    return player["base_attack"] + weapon_bonus.get(player["weapon_level"], 0)
def get_total_defense(player):
    armor_bonus = {0: 0, 1: 2, 2: 5, 3: 8}
    return player["base_defense"] + armor_bonus.get(player["armor_level"], 0)
def get_weapon_name(level):
    names = {0: "Нет", 1: "Меч новичка", 2: "Меч воина", 3: "Меч паладина"}
    return names.get(level, "Неизвестно")
def get_armor_name(level):
    names = {0: "Нет", 1: "Кожаная броня", 2: "Кольчуга", 3: "Литой нагрудник"}
    return names.get(level, "Неизвестно")
def add_health_potion(player, amount=1):
    player["inventory"]["health_potions"] += amount
def add_coins(player, amount):
    player["inventory"]["coins"] += amount