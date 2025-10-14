print('введите число')
number = int(input())
integer = 1
for i in range(number):
    integer *= (i+1)
print(integer)