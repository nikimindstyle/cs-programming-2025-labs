number = input("Введите число: ")

if not number.isdigit():
    print("Ошибка: введите целое положительное число")
else:
    last_digit = int(number[-1])
    digit_sum = sum(int(digit) for digit in number)
    
    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        print(f"Число {number} делится на 6")
    else:
        print(f"Число {number} не делится на 6")