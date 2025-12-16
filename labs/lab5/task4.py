f = input('введите значения через пробел: ')
g = tuple(f.split(' '))
h = True
for i in g:
    try:
        int(i)
    except:
        h = False
if h:
    g = tuple(sorted(g))
print(g)