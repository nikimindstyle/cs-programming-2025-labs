import random
a = []
for i in range(10):
    a.append(random.randint(0,10))
print(a)
for i in range(len(a)):
    if a[i] == 3:
        a[i] = 30
print(a)