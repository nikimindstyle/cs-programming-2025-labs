a, b, c = map(int, input("Введите три числа: ").split())

if a < b:
    smallest = a
else:
    smallest = b
if c < smallest:
    smallest = c
print(f"Наименьшее число: {smallest}")