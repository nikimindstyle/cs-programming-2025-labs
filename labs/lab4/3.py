try:
    dog_age = float(input("Введите возраст собаки (в годах):"))
    
    if dog_age < 1:
        print("ошибка!Возраст должен быть не меньше 1!")
    elif dog_age < 1:
        print("ошибка!Возраст должен быть не больше 22!")
    else:
        if dog_age <= 2:
            human_age = dog_age * 10.5
        else:
            human_age = 2 * 10.5 + (dog_age- 2) * 4
        
        print(f"Возраст собаки в человеческих годах: {human_age}")
except ValueError:
    print("Ошибка! Введите число!")        
