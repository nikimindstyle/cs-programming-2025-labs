from inventory import get_weapon_name, get_armor_name, add_health_potion

def shop(player):
    print("\nДобро пожаловать в магазин странствующего торговца! ")
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
            #...
            # выбор и покупка предметов, если хватает монет
            #...
        except ValueError:
            print("Пожалуйста, введите число.")