n = int(input("введите число"))
a = 0
b = 1
print("числа фибаначи до", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b