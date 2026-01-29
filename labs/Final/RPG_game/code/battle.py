def battle(player, enemy, can_flee=True):
    from inventory import get_total_attack, get_total_defense, use_health_potion

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
        #...
        # выбор действия и его реализация
        #...
                print("Не удалось убежать!")
        # Ход врага
        if enemy["hp"] > 0 and action != 3:
            damage = calculate_damage(enemy["attack"], total_def)
            player["hp"] -= damage
            print(f"{enemy['name']} наносит вам {damage} урона!")

        if player["hp"] <= 0:
            print("Вы погибли...")
            return "lose"

        print("-" * 30)

    return "win" if player["hp"] > 0 else "lose"