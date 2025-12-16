import random
c = []
for i in range(random.randint(1,1000)):
    c.append(random.randint(0,10000))
d = len(c)
e = max(c)
print(f'Длина: {d}, Макс: {e}')
print(e // d)