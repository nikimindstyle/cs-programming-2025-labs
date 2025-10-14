print('введите текст')
text = input()
str = ''
for i in range(len(text)):
    str += text[i] +f'{i+1}'
print(str)