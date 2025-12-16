ad = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
ae = {}
for af, ag in ad:
    ah = sum(ag) / len(ag)
    ae[af] = ah
print(ae)
ai = max(ae, key=ae.get)
aj = ae[ai]
print(f"{ai} имеет лучший балл: {aj}")