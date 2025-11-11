import random

list_of_numbers = []

for i in range(random.randint(0,100)):
    list_of_numbers.append(random.randint(0,100))

print(f'Данный список: {list_of_numbers}')

result = max(list_of_numbers) / len(list_of_numbers)

print(f'Результат операции: {result}')