amount = float(input("Введите сумму покупки: "))
if amount < 1000:
    discount_percent = 0
    discount_name = "0%"
elif 1000 <= amount <= 5000:
    discount_percent = 5
    discount_name = "5%"
elif 5000 < amount <= 10000:
    discount_percent = 10
    discount_name = "10%"
else:
    discount_percent = 15
    discount_name = "15%"

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount

print(f"Сумма покупки: {amount:.2f} руб.")
print(f"Ваша скидка: {discount_name} ({discount_amount:.2f} руб.)")
print(f"К оплате: {final_amount:.2f} руб.")