i = {"яблоко": 100, "банан": 80, "груша": 120}
j = ""
for k, l in i.items():
    if j == "" or i[j] < i[k]:
        j = k
print(f'Макс цена: {j} - {i[j]}')