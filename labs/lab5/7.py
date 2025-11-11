dict_of_words = {"Привет":"Hello","Досвидания":"Goodbye"}

user_input = input('введите слово на русском')

if(user_input in dict_of_words.keys()):
    print(f"слово {user_input}, перевод {dict_of_words[user_input]}")
else:
    print("В словаре нет такого слова")
