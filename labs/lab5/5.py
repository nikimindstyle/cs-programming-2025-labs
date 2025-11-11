import random

dict_of_goods = {"яблоко": random.randint(0,200), "банан": random.randint(0,200), "груша": random.randint(0,200), "фрутоняня":random.randint(0,200)}

print(f'Данный словарь: {dict_of_goods}')

max_price = 0
min_price = 200
for key, value in dict_of_goods.items():
    if(max_price < value): max_price = value
    if(min_price > value): min_price = value

print(f'результат операций: максимум: {max_price} минимум: {min_price}')