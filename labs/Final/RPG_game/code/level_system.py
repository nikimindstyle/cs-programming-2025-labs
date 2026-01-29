import random

def gain_exp(player, amount):
    player["exp"] += amount
    print(f"Вы получили {amount} опыта! Всего: {player['exp']}/{player['exp_to_next']}")
    if player["exp"] >= player["exp_to_next"]:
        level_up(player)

def level_up(player):
    player["level"] += 1
    hp_bonus = random.randint(15, 25)
    player["max_hp"] += hp_bonus
    player["hp"] = player["max_hp"]
    player["base_attack"] += random.randint(2, 4)
    player["base_defense"] += random.randint(1, 3)
    player["agility"] += random.randint(1, 2)
    player["exp_to_next"] = player["level"] * 100
    player["exp"] = 0
    print(f"\nПоздравляем! Вы достигли {player['level']} уровня!")
    print_status(player)