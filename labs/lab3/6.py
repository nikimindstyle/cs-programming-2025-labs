n = int(input("введите число"))
a = 0
b = 1
print("числа фибаначи до", n, ":")
while a <= n:
    print(a)
    a, b = b, a + b