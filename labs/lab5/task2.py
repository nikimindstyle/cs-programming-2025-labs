import random
b = []
for i in range(5):
    b.append(random.randint(0,100))
print(b)
for i in range(len(b)):
    b[i] = b[i] * b[i]
print(b)