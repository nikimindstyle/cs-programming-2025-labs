hour = int(input("Введите час (0-23): "))
if hour < 0 or hour > 23:
    print("Ошибка: введите число от 0 до 23")
elif hour <= 5:
    print("Сейчас ночь")
elif hour <= 11:
    print("Сейчас утро")
elif hour <= 17:
    print("Сейчас день")
else:
    print("Сейчас вечер")