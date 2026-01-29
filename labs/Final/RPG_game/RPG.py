import random

# ====== 1. СОЗДАНИЕ ПЕРСОНАЖА ======

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
    
    base_hp = random.randint(80, 100)
    base_attack = random.randint(8, 12)
    base_defense = random.randint(5, 9)
    base_agility = random.randint(8, 12)
    
    if choice == 1:  
        race_name = "Человек"
        hp = base_hp
        attack = base_attack
        defense = base_defense
        agility = base_agility
    elif choice == 2: 
        race_name = "Эльф"
        hp = random.randint(70, 90)
        attack = base_attack + 2
        defense = base_defense - 1
        agility = base_agility + 3
    else:  
        race_name = "Дворф"
        hp = random.randint(90, 110)
        attack = base_attack - 1
        defense = base_defense + 3
        agility = base_agility - 2

    attack = max(1, attack)
    defense = max(1, defense)
    agility = max(1, agility)

    character = {
        "name": "Герой",
        "race": race_name,
        "level": 1,
        "exp": 0,
        "exp_to_next": 100,
        "hp": hp,
        "max_hp": hp,
        "base_attack": attack,
        "base_defense": defense,
        "agility": agility,
        "weapon_level": 0,
        "armor_level": 0,
        "inventory": {
            "health_potions": 1,
            "coins": 50
        }
    }

    print("\nВаш персонаж создан!")
    print(f"Раса: {character['race']}")
    print(f"HP: {character['hp']}/{character['max_hp']}")
    print(f"Базовая атака: {character['base_attack']}")
    print(f"Базовая защита: {character['base_defense']}")
    print(f"Ловкость: {character['agility']}")
    print(f"Монеты: {character['inventory']['coins']}, Зелья: {character['inventory']['health_potions']}\n")

    return character


# ====== 2. СИСТЕМА СНАРЯЖЕНИЯ ======

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

def print_status(player):
    print(f"Раса: {player['race']}")
    print(f"Уровень: {player['level']}")
    print(f"HP: {player['hp']}/{player['max_hp']}")
    print(f"ATK: {get_total_attack(player)} (база {player['base_attack']} +{get_total_attack(player) - player['base_attack']})")
    print(f"DEF: {get_total_defense(player)} (база {player['base_defense']} +{get_total_defense(player) - player['base_defense']})")
    print(f"AGI: {player['agility']}")
    print(f"Оружие: {get_weapon_name(player['weapon_level'])}")
    print(f"Броня: {get_armor_name(player['armor_level'])}")
    print(f"Монеты: {player['inventory']['coins']}, Зелья: {player['inventory']['health_potions']}\n")


# ====== 3. ГЕНЕРАЦИЯ КОМНАТЫ ======

def generate_room():
    return random.choice(["battle", "chest", "rest"])

def room_name(room_type):
    names = {"battle": "Бой", "chest": "Сундук", "rest": "Отдых"}
    return names.get(room_type, "???")


# ====== 4. ИНВЕНТАРЬ ======

def use_health_potion(player):
    if player["inventory"]["health_potions"] > 0:
        heal_amount = 30
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
        player["inventory"]["health_potions"] -= 1
        print(f"Вы выпили зелье и восстановили {heal_amount} HP!")
        return True
    else:
        print("У вас нет зелий лечения!")
        return False

def add_health_potion(player, amount=1):
    player["inventory"]["health_potions"] += amount

def add_coins(player, amount):
    player["inventory"]["coins"] += amount


# ====== 5. ВРАГИ ======

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


# ====== 6. БОЙ ======

def calculate_damage(attacker_atk, defender_def):
    damage = attacker_atk - defender_def
    return max(1, damage)

def battle(player, enemy, can_flee=True):
    """
    Проводит бой.
    can_flee — можно ли убежать (у мимика — нельзя)
    """
    print(f"\nВы встречаете {enemy['name']}! (HP: {enemy['hp']})")
    print("Бой начался!\n")
    
    while player["hp"] > 0 and enemy["hp"] > 0:
        total_atk = get_total_attack(player)
        total_def = get_total_defense(player)
        
        print(f"Ваше HP: {player['hp']}/{player['max_hp']} | {enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
        print("(1) Атаковать")
        print("(2) Использовать зелье")
        if can_flee:
            print("(3) Попытаться убежать")
        else:
            print("(3) Убежать невозможно!")
        
        while True:
            try:
                action = int(input("> "))
                if action in [1, 2, 3]:
                    if action == 3 and not can_flee:
                        print("Вы не можете убежать от мимика!")
                        continue
                    break
                else:
                    print("Введите 1, 2 или 3.")
            except ValueError:
                print("Пожалуйста, введите число.")
        
        if action == 1:
            damage = calculate_damage(total_atk, enemy["defense"])
            enemy["hp"] -= damage
            print(f"Вы наносите {damage} урона!")
            if enemy["hp"] <= 0:
                print(f"{enemy['name']} повержен!")
                return "win"
        elif action == 2:
            use_health_potion(player)
        elif action == 3:
            if random.random() < 0.5:
                print("Вы убегаете из боя!")
                return "flee"
            else:
                print("Не удалось убежать!")
        
        if enemy["hp"] > 0 and action != 3:
            damage = calculate_damage(enemy["attack"], total_def)
            player["hp"] -= damage
            print(f"{enemy['name']} наносит вам {damage} урона!")
            if player["hp"] <= 0:
                print("Вы погибли...")
                return "lose"
        
        print("-" * 30)
    
    return "win" if player["hp"] > 0 else "lose"


# ====== 7. СУНДУК ИЛИ МИМИК ======

def chest_loot(player):
    """Выдаёт обычный лут сундука"""
    coins = random.randint(10, 30)
    add_coins(player, coins)
    print(f"Вы нашли сундук! Внутри: {coins} монет.")
    
    if random.random() < 0.6:
        add_health_potion(player, 1)
        print("Также вы нашли зелье лечения!")
    
    print(f"Монеты: {player['inventory']['coins']}, Зелья: {player['inventory']['health_potions']}")

def open_chest(player):
    """Открывает сундук. С 30% шанс — мимик!"""
    if random.random() < 0.3:  # 30% шанс
        print("Сундук оживает! Это МИМИК!")
        mimic = create_mimic()
        result = battle(player, mimic, can_flee=False)
        if result == "win":
            print("Вы победили мимика! Он превращается в настоящий сундук...")
            chest_loot(player)  # даёт обычный лут
            # Опыт в 2 раза больше
            exp_gain = random.randint(20, 50) * 2
            gain_exp(player, exp_gain)
        elif result == "lose":
            # игра закончится в основном цикле
            pass
        return result
    else:
        print("Обычный сундук...")
        chest_loot(player)
        return "safe"


# ====== 8. МАГАЗИН ======

def shop(player):
    print("\n Добро пожаловать в магазин странствующего торговца! ")
    print("У вас:", player["inventory"]["coins"], "монет")
    print(f"\nВаше оружие: {get_weapon_name(player['weapon_level'])}")
    print(f"Ваша броня: {get_armor_name(player['armor_level'])}")
    
    can_upgrade_weapon = player["weapon_level"] < 3
    can_upgrade_armor = player["armor_level"] < 3
    
    print("\nТовары:")
    if can_upgrade_weapon:
        next_weapon = get_weapon_name(player["weapon_level"] + 1)
        price = 50 * (player["weapon_level"] + 1)
        print(f"1) Улучшить оружие до «{next_weapon}» — {price} монет")
    else:
        print("1) У вас лучшее оружие!")
    
    if can_upgrade_armor:
        next_armor = get_armor_name(player["armor_level"] + 1)
        price = 40 * (player["armor_level"] + 1)
        print(f"2) Улучшить броню до «{next_armor}» — {price} монет")
    else:
        print("2) У вас лучшая броня!")
    
    print("3) Зелье лечения (+30 HP) — 20 монет")
    print("0) Выйти из магазина")
    
    while True:
        try:
            choice = int(input("\nЧто купить? > "))
            if choice == 0:
                print("Вы покидаете магазин.")
                break
            elif choice == 1 and can_upgrade_weapon:
                price = 50 * (player["weapon_level"] + 1)
                if player["inventory"]["coins"] >= price:
                    player["inventory"]["coins"] -= price
                    player["weapon_level"] += 1
                    print(f"Вы улучшили оружие до «{get_weapon_name(player['weapon_level'])}»!")
                else:
                    print("Недостаточно монет!")
            elif choice == 2 and can_upgrade_armor:
                price = 40 * (player["armor_level"] + 1)
                if player["inventory"]["coins"] >= price:
                    player["inventory"]["coins"] -= price
                    player["armor_level"] += 1
                    print(f"Вы улучшили броню до «{get_armor_name(player['armor_level'])}»!")
                else:
                    print("Недостаточно монет!")
            elif choice == 3:
                if player["inventory"]["coins"] >= 20:
                    player["inventory"]["coins"] -= 20
                    add_health_potion(player, 1)
                    print("Вы купили зелье лечения!")
                else:
                    print("Недостаточно монет!")
            else:
                print("Неверный выбор или улучшение недоступно.")
        except ValueError:
            print("Пожалуйста, введите число.")


# ====== 9. ОПЫТ И УРОВНИ ======

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
    
    print(f"\n Поздравляем! Вы достигли {player['level']} уровня!")
    print_status(player)


# ====== 10. ИГРОВОЙ ЦИКЛ ======

def game_loop(player):
    print("Вы входите в тёмное подземелье...\n")
    
    while player["hp"] > 0:
        print("Перед вами развилка.")
        
        left_room = generate_room()
        right_room = generate_room()
        
        left_visible = random.choice([True, False])
        right_visible = random.choice([True, False])
        
        left_text = room_name(left_room) if left_visible else "???"
        right_text = room_name(right_room) if right_visible else "???"
        
        print(f"(1) Слева: {left_text}")
        print(f"(2) Справа: {right_text}")
        
        while True:
            try:
                choice = int(input("\nКуда пойти? (1 или 2) > "))
                if choice in [1, 2]:
                    break
                else:
                    print("Введите 1 или 2.")
            except ValueError:
                print("Пожалуйста, введите число.")
        
        chosen_room = left_room if choice == 1 else right_room
        print(f"\nВы заходите в комнату: {room_name(chosen_room)}\n")
        
        if chosen_room == "battle":
            enemy = create_enemy()
            result = battle(player, enemy, can_flee=True)
            if result == "win":
                exp_gain = random.randint(20, 50)
                gain_exp(player, exp_gain)
            elif result == "lose":
                break
        elif chosen_room == "chest":
            result = open_chest(player)
            if result == "lose":
                break
        elif chosen_room == "rest":
            heal = int(player["max_hp"] * 0.3)
            player["hp"] = min(player["max_hp"], player["hp"] + heal)
            print(f"Вы отдыхаете и восстанавливаете {heal} HP.")
            shop(player)
        
        print("\n" + "="*40 + "\n")
    
    print("Игра окончена.")


# ====== ЗАПУСК ======
if __name__ == "__main__":
    player = create_character()
    game_loop(player)