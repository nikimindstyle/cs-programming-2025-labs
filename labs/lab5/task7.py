q = {"Hello" : 'Привет', 'Bye' : "Пока"}
r = input('введите слово на русском: ')
s = False
for t, u in q.items():
    if u == r:
        print(t)
        s = True
        break
if not s:
    print('Нет такого слова')

