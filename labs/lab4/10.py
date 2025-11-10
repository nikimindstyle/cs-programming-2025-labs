try:
    number = int(input("Введите число: "))
    
    if number < 2:
        print(f"{number} - не является простым числом")
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{number} - простое число")
        else:
            print(f"{number} - составное число")

except ValueError:
    print("Ошибка: введите целое число!")